"""Build world.json (v2.5) from world_original.json (v2.4).

Every edit is an exact-match replacement that asserts it matched once, so an
edit can never silently fail. Adult content and tracker values are untouched.
"""
import json
import pathlib

ROOT = pathlib.Path(__file__).resolve().parent.parent
d = json.loads((ROOT / "world_original.json").read_text(encoding="utf-8"))
log = []


def sub(text, old, new, where):
    n = text.count(old)
    assert n == 1, f"{where}: expected 1 match, found {n}: {old[:70]!r}"
    log.append(where)
    return text.replace(old, new)


def field(key, old, new, label):
    d[key] = sub(d[key], old, new, f"{key}: {label}")


def block(bid):
    return next(b for b in d["instructionBlocks"] if b["id"] == bid)


def blk(bid, old, new, label):
    b = block(bid)
    b["content"] = sub(b["content"], old, new, f"block {bid}: {label}")


def lore(lid):
    return next(x for x in d["loreBookEntries"] if x["id"] == lid)


def trigger_effect(tid):
    return next(t for t in d["triggerEvents"] if t["id"] == tid)["triggerEffects"][0]["data"]


# ---------------------------------------------------------------- B: bugs
# B1 skills: native skill panel duplicated SKILLS & TRAINING and went stale.
d["hideSkillSystem"] = True
d["allowChangeCharacterSkills"] = False
log.append("hideSkillSystem=true, allowChangeCharacterSkills=false (SKILLS & TRAINING is the single skill owner)")

# B2 combat rules were loaded from turn 1; every other dynamic block starts empty.
block("DYNAMIC_COMBAT")["content"] = ""
log.append("block DYNAMIC_COMBAT: start empty (COMBAT_START trigger loads it)")

# B3 CORE_SKILLS contradicted itself and the evaluation contract about rolling dice.
blk("CORE_SKILLS",
    "OPTIONAL D100: only when a roll is useful, roll d100 <= modified skill.",
    "OPTIONAL D100: only when the game or player actually supplies a roll, resolve it as d100 <= modified skill; never fabricate a roll.",
    "D100 only when a roll is supplied (matched evaluation contract)")

# ------------------------------------------------- A: duplicate consolidation
# descriptionRequest
field("descriptionRequest",
      '    sensing:\n'
      '      - "Ordinary senses provide ordinary evidence."\n'
      '      - "Campione physiology may enhance defined physical senses; it does not automatically identify foreign metaphysics."\n'
      '      - "Ahriman\'s constant burden may be felt as background pressure/whispers, but specific sins, identities or culpability records require deliberate targeted Ledger use or an already-established record."\n'
      '      - "Never invent \'mana density\', hidden reserve size, exact power signatures or system labels without a valid recorded sense."\n',
      '    sensing:\n'
      '      - "Ordinary senses provide ordinary evidence. Campione physiology may enhance defined physical senses; it does not automatically identify foreign metaphysics."\n'
      '      - "Apply CORE_SENSING (Ahriman whisper limits, no passive mana/reserve/signature diagnosis) and CORE_PERCEPTION_AND_KNOWLEDGE."\n',
      "sensing -> pointers to CORE_SENSING/PERCEPTION")
field("descriptionRequest",
      '      - "Do not reset intimacy: a long-term partner, friend, rival or family-like bond should sound like one."\n'
      '      - "On a character\'s first meaningful appearance, give 1-3 distinctive visible appearance cues; on later appearances repeat only changed/relevant details rather than redescribing them every scene."\n',
      '      - "Do not reset intimacy: a long-term partner, friend, rival or family-like bond should sound like one."\n',
      "removed 2nd copy of appearance rule")
field("descriptionRequest",
      '      - "Before substantial dialogue, recover speaker goal, listener, stress, relationship register, unresolved topic, relevant shared memory and actual knowledge."\n'
      '      - "Do not make dialogue alternate mechanically speaker-by-speaker; use interruptions, pauses, overlap, silence and delayed answers naturally."\n'
      '      - "Avoid exposition both speakers already know. Let them reference shared history in shorthand."\n'
      '      - "Different characters should differ in cadence, formality, humor, profanity, evasion, directness and conflict style."\n',
      '      - "Run CORE_VOICE_GATE silently before substantial named-character dialogue; follow authorStyle.dialogue and CORE_NATURAL_SPEECH."\n',
      "dialogue duplicates -> pointer to VOICE_GATE/authorStyle")

# evaluationRequest
field("evaluationRequest",
      '        - "No ambient detailed Ledger read; targeted Ahriman reading requires deliberate intent and a uniquely identified subject."\n'
      '        - "Do not invent generic Authority headaches, focus fatigue, nosebleeds or exhaustion when authored costs/counters already govern the effect."\n'
      '        - "No passive \'mana/power signature/reserve\' diagnosis unless an established sense explicitly supports it."\n',
      '        - "Apply CORE_SENSING: no ambient detailed Ledger read; no passive mana/signature/reserve diagnosis."\n',
      "knowledge_sensing duplicates -> pointer")
field("evaluationRequest",
      '        - "Do not invent generic focus/fatigue/self-damage taxes for Authority use; use authored costs, counters, injuries and suppression only."\n',
      '',
      "time_resources: removed fatigue repeat (owned by CORE_RESOURCE_RESOLUTION + hard rule)")
field("evaluationRequest",
      '        - "NPC action requires goal/motive, knowledge, memory, opportunity, capability and time."\n'
      '        - "Advance offscreen plans only when prerequisites exist."\n',
      '',
      "npc_world_motion: removed 2 repeats of the CORE_WORLD_MOTION prerequisite rule")
field("evaluationRequest",
      '        - "Apply CORE_NPC_DRIVES and CORE_WORLD_MOTION.',
      '        - "Apply CORE_NPC_BEHAVIOR and CORE_WORLD_MOTION.',
      "reference updated (NPC_DRIVES merged into NPC_BEHAVIOR)")

# instructions (only the reference; adult section untouched)
field("instructions",
      "CORE_EMOTIONAL_STATE, CORE_NPC_DRIVES, CORE_WORLD_MOTION",
      "CORE_EMOTIONAL_STATE, CORE_NPC_BEHAVIOR, CORE_WORLD_MOTION",
      "reference updated (NPC_DRIVES merged into NPC_BEHAVIOR)")

# CORE_VOICE_GATE: same sentence twice in one block
blk("CORE_VOICE_GATE",
    "Style fingerprints are tendencies, not quotas. Never force sentence-length variation, interruptions, pauses, body tells, callbacks, profanity or paragraph structure merely to satisfy the voice system.\n",
    "",
    "removed sentence duplicated inside the same block")
# CORE_NATURAL_SPEECH: quota rule is owned by VOICE_GATE; mode rule owned by DM_MODE
blk("CORE_NATURAL_SPEECH",
    '  - "Treating voice fingerprints as quotas: never force sentence-length variation, interruption, pauses, profanity, body tells, callbacks or paragraph shapes merely to satisfy the style system."\n',
    "",
    "removed quota repeat (owned by CORE_VOICE_GATE)")
blk("CORE_NATURAL_SPEECH",
    'dm_mode: "DM Mode changes prose register, not truth, difficulty, knowledge or NPC intelligence. Do not announce the mode."\n',
    "",
    "removed DM-mode repeat (owned by CORE_DM_MODE)")

# CORE_PARAMETERS: regen ranks duplicated CORE_TIME
blk("CORE_PARAMETERS",
    '  resource_rank_values: "For CHA True Ether regeneration only: E1,E+1.5,D2,D+2.5,C3,C+3.5,B4,B+4.5,A5,A+5.5,S6,S+7,EX8. H-ranks grant no True Ether regeneration unless a separate rule explicitly says so."\n',
    '  resource_rank_values: "True Ether regeneration ranks/table live in CORE_TIME; H-ranks grant none."\n',
    "regen rank values -> pointer to CORE_TIME")

# NPC_DRIVES merged into NPC_BEHAVIOR (all unique lines kept verbatim)
blk("CORE_NPC_BEHAVIOR",
    'formula: "personality + values + current goal + knowledge/belief + relationship + emotion/stress + culture/role + perceived risk + available options"\n',
    'formula: "personality + values + current goal + knowledge/belief + relationship + emotion/stress + culture/role + dominant drive + perceived risk + available options"\n'
    'drives:\n'
    '  possible: "preservation/safety; certainty/closure; comfort/rest/pleasure; belonging/tribal affiliation; legacy/family/mentorship; curiosity/novelty; disgust/avoidance; meaning/transcendence; status/control/autonomy. Not every character values every drive equally."\n'
    '  rule: "Drives create pressure, not compulsion. They never force touching, violence, theft, romance, sex, confession, stupidity or hostility without character-specific motive/opportunity."\n',
    "merged CORE_NPC_DRIVES drives list + pressure-not-compulsion rule")
blk("CORE_NPC_BEHAVIOR",
    '  - "Status and social context matter: guards guard, parents protect, rulers weigh legitimacy, professionals have duties, criminals protect leverage, civilians prioritize safety."\n'
    '  - "Offscreen action requires information, motive, opportunity, capability and time."\n',
    '  - "Status and social context matter: guards guard, parents protect, rulers weigh legitimacy, professionals have duties, criminals protect leverage, civilians prioritize safety; individuals can still violate their role for a believable reason."\n',
    "role rule absorbs NPC_DRIVES nuance; offscreen repeat removed (owned by CORE_WORLD_MOTION)")
d["instructionBlocks"] = [b for b in d["instructionBlocks"] if b["id"] != "CORE_NPC_DRIVES"]
log.append("block CORE_NPC_DRIVES removed after merge into CORE_NPC_BEHAVIOR")

# LONG_TERM_MEMORY merged into MEMORY_LIFECYCLE (unique lines kept)
blk("CORE_MEMORY_LIFECYCLE",
    'plans: "Offscreen action requires information, motive, opportunity, capability and enough time."\n',
    'promotion_test: "Keep a memory if a recurring character would behave differently were it forgotten; if it creates/alters a promise, debt, boundary, secret, sore point, joke, nickname, habit, reputation or obligation; or if it changes a character arc, canon prerequisite, investigation, location familiarity, meaningful object or revisit state."\n'
    'memory_effect: "Memory affects initiative, shorthand, trust, conflict and emotional register even when not explicitly referenced. A topic ends only when answered, consciously dropped, interrupted beyond relevance or resolved by events."\n'
    'revisit: "On return to an old world, restore surviving important NPCs, Nikola\'s reputation, political/local consequences, assets/ties left there and unresolved hooks before unchanged canon."\n',
    "merged unique CORE_LONG_TERM_MEMORY rules; offscreen repeat removed")
d["instructionBlocks"] = [b for b in d["instructionBlocks"] if b["id"] != "CORE_LONG_TERM_MEMORY"]
log.append("block CORE_LONG_TERM_MEMORY removed after merge into CORE_MEMORY_LIFECYCLE (summary budget stays in summaryRequest)")

# Lore entries that repeated always-on blocks
ether = lore("ETHER_LORE")
start = ether["content"].index("REGENERATION\n")
end = ether["content"].index("COST GUIDANCE\n")
ether["content"] = (ether["content"][:start]
                    + "REGENERATION & TIME ACCOUNTING\n"
                    "Use live CHA with the regeneration table and accounting rules in CORE_TIME / CORE_RESOURCE_RESOLUTION (always loaded).\n"
                    "Regeneration continues during Authority use unless a specific established effect suppresses it.\n\n"
                    + ether["content"][end:])
log.append("lore ETHER_LORE: regen table + time accounting -> pointer (kept unique cost guidance)")

attr = lore("ATTRIBUTE_SCALE_LORE")
attr["content"] = (
    "ATTRIBUTE SCALE — HUMAN / SUB-E / FATE RANKS\n\n"
    "The full ladder and comparison rules are in CORE_PARAMETERS (always loaded). E is not the minimum stat; ordinary humans are H1-H3.\n\n"
    "H2 also covers experienced manual workers. Reinforcement does not rewrite a magus's permanent base stats.\n\n"
    "TEMPORARY EFFECTIVE STATS NOTATION\n"
    "base STR: H2\n"
    "effective STR: H8 (Reinforcement active)\n"
    "When the effect ends, the base remains H2 unless a real permanent change occurred."
)
log.append("lore ATTRIBUTE_SCALE_LORE: duplicate of CORE_PARAMETERS -> pointer + unique notation example")

skl = lore("SKILL_SYSTEM_LORE")
start = skl["content"].index("SEPARATE PF2E-STYLE PERCEPTION\n")
end = skl["content"].index("STARTING RATINGS\n")
skl["content"] = skl["content"][:start] + "PERCEPTION & POWER PROFICIENCIES\nTracked separately from the skill list; see CORE_SKILLS.\n\n" + skl["content"][end:]
start = skl["content"].index("ADVANCEMENT\n")
skl["content"] = skl["content"][:start] + (
    "ADVANCEMENT\nGrowth amounts follow CORE_SKILLS. Do not award proficiency merely for possessing an Authority, "
    "seeing a technique once or succeeding through raw stats.")
log.append("lore SKILL_SYSTEM_LORE: perception/power/advancement repeats -> pointer (kept domain definitions)")

earth = lore("EARTH_LORE")
start = earth["content"].index("CONTINUITY OF THE AUDIENCE\n")
end = earth["content"].index("PUBLIC ARC AFTER CAMPIONE\n")
earth["content"] = (earth["content"][:start]
                    + "Continuity and reaction rules: CORE_EARTH_CONTINUITY (always loaded). "
                    "Source-fandom viewers may recognize settings/canon that Nikola does not.\n\n"
                    + earth["content"][end:])
log.append("lore EARTH_LORE: continuity/reaction repeats -> pointer (kept public arc, memes, world-selection note)")

# --------------------------------------------------- C: over-broad keywords
def drop_keywords(lid, words):
    entry = lore(lid)
    before = list(entry["keywords"])
    for w in words:
        assert w in entry["keywords"], f"{lid}: keyword {w!r} missing"
    entry["keywords"] = [k for k in before if k not in words]
    log.append(f"lore {lid}: removed keywords {words}")

drop_keywords("AHRIMAN_LORE", ["whispers", "malice", "corruption"])
drop_keywords("CHERNOBOG_LORE", ["Forsaken", "Forgotten", "Forbidden", "Frozen"])
drop_keywords("TRAITS_LORE", ["Campione"])
drop_keywords("SKILL_SYSTEM_LORE", ["Acrobatics", "Arcana", "Athletics", "Crafting", "Deception", "Diplomacy",
                                    "Intimidation", "Medicine", "Nature", "Occultism", "Performance", "Religion",
                                    "Society", "Stealth", "Survival", "Thievery", "teacher"])
drop_keywords("ATTRIBUTE_SCALE_LORE", ["E+", "A+", "S+"])

# ----------------------------------------------------------- D: prose style
field("authorStyle",
      '  dm_mode: "Read the DM Mode tracker and DM_MODE_LORE. Modes change prose register, not world rules, knowledge or difficulty."\n',
      '  dm_mode: "Read the DM Mode tracker and CORE_DM_MODE. Modes change prose register, not world rules, knowledge or difficulty."\n'
      '  example_note: "STYLE REFERENCE ONLY. It shows rhythm, dialogue texture and how a scene ends. It is not an event, not canon and not a template: never reuse its people, lines, objects or situation. Narrative person/viewpoint follows outcome_description.viewpoint_person, not this sample."\n'
      '  example_passage: |\n'
      '    The door sticks halfway. Nikola shoulders it the rest of the way and the frame groans like it has opinions.\n'
      '    Inside, the quartermaster doesn\'t look up. She\'s counting bolts into a tin, lips moving, and raises one finger without breaking rhythm.\n'
      '    Nikola waits. The whispers don\'t. They never do; they sit under everything like traffic from a city made of bad decisions.\n'
      '    "Forty." She snaps the tin shut and finally looks at him. Then at the blood drying on his sleeve. Then back at his face, deciding which problem is bigger. "That yours?"\n'
      '    "Mostly."\n'
      '    "Mostly." She drags a ledger over and writes something that is definitely not his name. "Last man who said mostly to me tried to sell me his partner\'s boots an hour later."\n'
      '    "Were they good boots?"\n'
      '    A breath through the nose that isn\'t quite a laugh. She slides a key across the counter and keeps two fingers on it.\n'
      '    "Room\'s upstairs. Don\'t bleed on the stairs; the owner counts the stains." A pause. "Whoever you left mostly alive. They coming here?"\n',
      "added style reference passage; fixed broken DM_MODE_LORE reference -> CORE_DM_MODE")
field("descriptionRequest",
      '  language: "Present tense."\n',
      '  language: "Present tense."\n'
      '  viewpoint_person: "Mirror the narrative person and focal character the player\'s latest input uses (I / you / Nikola / another character). If the player switches person or character, follow the switch; otherwise keep the one last used."\n',
      "added viewpoint-mirroring rule")

# -------------------------------------------------------------- metadata
d["version"] = "2.5-long-campaign-authority-growth-simulation-dialogue-consolidated"
d["description"] = d["description"].replace("v2.4 long-campaign", "v2.5 long-campaign", 1)
d["designNotes"] += (
    "\n\nv2.5 Consolidation pass:\n"
    "- Merged duplicated rules into single owners (CORE_NPC_DRIVES -> CORE_NPC_BEHAVIOR; CORE_LONG_TERM_MEMORY -> CORE_MEMORY_LIFECYCLE); "
    "intentional reinforcement kept in hard_rules, final_check and the owning block.\n"
    "- Lore entries that repeated always-on blocks now point to them; over-broad lore keywords removed.\n"
    "- Fixes: authorStyle DM_MODE_LORE reference -> CORE_DM_MODE; native skill panel hidden (SKILLS & TRAINING is sole owner); DYNAMIC_COMBAT starts empty; D100 only when a roll is supplied.\n"
    "- Added authorStyle example_passage and viewpoint_person mirroring rule.\n"
    "- Adult-mode section, Sexual descriptor tracker and all tracker starting values unchanged."
)

out = ROOT / "world.json"
out.write_text(json.dumps(d, ensure_ascii=False, indent=4), encoding="utf-8")
print("\n".join(f"- {x}" for x in log))
