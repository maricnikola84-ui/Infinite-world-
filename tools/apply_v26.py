"""Build world.json (v2.6): regenerate v2.5 from world_original.json, then apply v2.6.

All new text comes from v26_content.py (the reviewed REVIEW_v26.md). Every edit to
existing text is an exact-match replacement that asserts it matched once.
"""
import hashlib
import json
import pathlib
import runpy

import v26_content as c

ROOT = pathlib.Path(__file__).resolve().parent.parent
runpy.run_path(str(ROOT / "tools" / "apply_v25.py"), run_name="__main__")
d = json.loads((ROOT / "world.json").read_text(encoding="utf-8"))
log = []

DM_MODE_TRACKER_ID = next(t["id"] for t in d["trackedItems"] if t["name"] == "DM Mode")


def uid(prefix, *parts):
    return prefix + hashlib.sha1("|".join(parts).encode()).hexdigest()[:9]


def sub(text, old, new, where):
    n = text.count(old)
    assert n == 1, f"{where}: expected 1 match, found {n}: {old[:70]!r}"
    log.append(where)
    return text.replace(old, new)


def block(bid):
    return next(b for b in d["instructionBlocks"] if b["id"] == bid)


def trigger_data(tid):
    return next(t for t in d["triggerEvents"] if t["id"] == tid)["triggerEffects"][0]["data"]


def insert_block_after(after_id, new_block):
    i = next(i for i, b in enumerate(d["instructionBlocks"]) if b["id"] == after_id)
    d["instructionBlocks"].insert(i + 1, new_block)


def add_tracker(spec, tid, var):
    d["trackedItems"].append({
        "id": tid, "name": spec["name"], "positionInList": len(d["trackedItems"]),
        "dataType": "text", "visibility": spec["visibility"],
        "description": spec["description"], "updateInstructions": spec["updateInstructions"],
        "formatExample": spec["formatExample"], "enforceFormat": False, "formatSchema": "",
        "initialValue": spec["initialValue"], "initialValueBasedOnPC": "same",
        "autoUpdate": True, "variableName": var, "driftAcknowledgedForName": None,
    })
    log.append(f"tracker added: {spec['name']} ({spec['visibility']})")


# ------------------------------------------------------------ 1. Canon accuracy
insert_block_after("CORE_PERCEPTION_AND_KNOWLEDGE",
                   {"id": "CORE_CANON_FIDELITY", "name": "Canon Fidelity", "content": c.CANON_FIDELITY_BLOCK})
log.append("block added: CORE_CANON_FIDELITY")
d["instructions"] = sub(
    d["instructions"],
    '    - "When canon threats matter, apply CORE_WORLD_THREAT: preserve canon capability without downscaling or artificial stat inflation."\n',
    '    - "When canon threats matter, apply CORE_WORLD_THREAT: preserve canon capability without downscaling or artificial stat inflation."\n'
    '    - "Apply CORE_CANON_FIDELITY and the WORLD CANON SHEET so each universe\'s own terms and cosmology stay accurate and never blend with another franchise."\n',
    "instructions: hard rule pointing to CORE_CANON_FIDELITY")
add_tracker(c.CANON_SHEET_TRACKER, "WORLD_CANON_SHEET", "world_canon_sheet")
d["loreBookEntries"].append({"id": "TYPE_MOON_PRIMER", "name": c.TYPE_MOON_PRIMER["name"],
                             "content": c.TYPE_MOON_PRIMER["content"], "keywords": c.TYPE_MOON_PRIMER["keywords"]})
log.append("lore added: TYPE_MOON_PRIMER")

# ------------------------------------------------------------ 2. DM Mode pack
core = block("CORE_DM_MODE")
assert core["content"].startswith("DM MODE — ADAPTIVE JUMPER NARRATION")
core["content"] = c.DM_MODE_CORE
log.append("block CORE_DM_MODE: replaced with summary + ACTIVE MODE BLOCKS rule")

prev = "CORE_DM_MODE"
for suffix, title, subs, focus, do, avoid, example in c.DM_MODES:
    bid = f"DM_MODE_{suffix}"
    content = (f"<dm_mode_active>\n"
               f"ACTIVE DM MODE: {title}. Register only; never changes rules, knowledge, difficulty or consent.\n"
               f"focus: \"{focus}\"\n"
               f"do: \"{do}\"\n"
               f"avoid: \"{avoid}\"\n"
               f"sound_reference (not an event; never reuse its people, objects or lines): \"{example}\"\n"
               f"</dm_mode_active>")
    # Tracker starts at "lived", so only LIVED is loaded at game start.
    insert_block_after(prev, {"id": bid, "name": f"DM Mode — {title} (auto)",
                              "content": content if suffix == "LIVED" else ""})
    prev = bid
    variants = []
    for s in subs:
        for v in (s, s.capitalize(), s.upper()):
            if v not in variants:
                variants.append(v)

    def conds(kind):
        return [{"id": uid("cond_", bid, kind, v), "type": "triggerOnTrackedItem", "category": "condition",
                 "trackedItemID": DM_MODE_TRACKER_ID,
                 "data": {"inequality": "is_exactly", "requiredValue": v,
                          "textComparison": "contains", "trackedItemID": DM_MODE_TRACKER_ID}}
                for v in variants]

    for kind, operator, text in (("on", "or", content), ("off", "none_of", "")):
        d["triggerEvents"].append({
            "id": f"{bid}_{kind.upper()}",
            "name": f"DM Mode {title}: {'load' if kind == 'on' else 'unload'} guide",
            "advancedLogic": True,
            "triggerEffects": [{"id": uid("eff_", bid, kind), "type": "effectModifyInstructionBlock",
                                "data": {"id": bid, "content": text}}],
            "triggerConditions": [{"id": uid("logic_", bid, kind), "category": "logic",
                                   "operator": operator, "data": conds(kind)}],
            "canTriggerMoreThanOnce": True,
        })
log.append(f"12 DM_MODE_* blocks + 24 load/unload triggers reading DM Mode tracker {DM_MODE_TRACKER_ID}")

d["descriptionRequest"] = sub(
    d["descriptionRequest"],
    '    - "Exactly one SECRETINFO block?"\n',
    '    - "Exactly one SECRETINFO block?"\n'
    f'    - "{c.DM_MODE_FINAL_CHECK}"\n',
    "descriptionRequest: final check for DM Mode register (last line)")
d["authorStyle"] = sub(
    d["authorStyle"],
    "Read the DM Mode tracker and CORE_DM_MODE.",
    "Read the DM Mode tracker, CORE_DM_MODE and the active DM_MODE_* blocks.",
    "authorStyle: points to active DM_MODE_* blocks")

# ------------------------------------------------------------ 3. New trackers
add_tracker(c.WORLD_GOALS_TRACKER, "WORLD_GOALS", "world_goals")
add_tracker(c.FACTIONS_TRACKER, "FACTIONS_REPUTATION", "factions_and_reputation")
add_tracker(c.ASCENDANT_VIEWS_TRACKER, "ASCENDANT_VIEWS", "ascendant_views")

own = block("CORE_STATE_OWNERSHIP")
own["content"] = sub(own["content"],
                     '  DM_TRUTH_KNOWLEDGE: "Compact consequential secret/knowledge gates."\n',
                     '  DM_TRUTH_KNOWLEDGE: "Compact consequential secret/knowledge gates."\n' + c.OWNERSHIP_ADDITIONS,
                     "block CORE_STATE_OWNERSHIP: new trackers listed")
d["summaryRequest"] = sub(
    d["summaryRequest"],
    'keep: "Current player-established goals only; do not invent compulsory campaign objectives beyond the standing thousand-world premise."',
    f'keep: "Current player-established goals only; do not invent compulsory campaign objectives beyond the standing thousand-world premise. {c.SUMMARY_OBJECTIVES_NOTE}"',
    "summaryRequest: objectives defer to WORLD GOALS")

asc = trigger_data("ASCENDANT_CONTACT")
asc["content"] = sub(asc["content"], "</dynamic_ascendant_contact>",
                     c.ASCENDANT_CONTACT_ADDITION + "</dynamic_ascendant_contact>",
                     "trigger ASCENDANT_CONTACT: use ASCENDANT VIEWS")

entry_anchor = '  - "Rewrite SCENE STATE to the real arrival snapshot and CURRENT CAST to only immediately relevant actors."\n'
entry_block = block("DYNAMIC_WORLD_ENTRY")
entry_block["content"] = sub(entry_block["content"], entry_anchor, entry_anchor + c.WORLD_ENTRY_ADDITION,
                             "block DYNAMIC_WORLD_ENTRY: write WORLD CANON SHEET")
entry_trig = trigger_data("WORLD_ENTRY")
entry_trig["content"] = sub(entry_trig["content"], entry_anchor, entry_anchor + c.WORLD_ENTRY_ADDITION,
                            "trigger WORLD_ENTRY: write WORLD CANON SHEET")

crossing, clear_line, ascendant_line = c.WORLD_EXIT_ADDITIONS.splitlines(keepends=True)
exit_trig = trigger_data("WORLD_EXIT")
resolve = '  - "Resolve surviving injuries/effects first; confirm powers, assets and companions that actually cross."\n'
exit_trig["content"] = sub(exit_trig["content"], resolve, resolve + crossing, "trigger WORLD_EXIT: crossing rule")
clear = '  - "Clear local live cast/scene/plans only after retention."\n'
exit_trig["content"] = sub(exit_trig["content"], clear, clear_line + ascendant_line + clear,
                           "trigger WORLD_EXIT: archive/clear new trackers, review ASCENDANT VIEWS")

prem = block("CORE_PREMISE")
prem["content"] = sub(prem["content"], "mystery_pacing:", c.PREMISE_CROSSING_LINE + "mystery_pacing:",
                      "block CORE_PREMISE: crossing rule")

# ------------------------------------------------------------ 4. Story engine
adult_at = d["instructions"].index("<adult_mode>")
adult_before = d["instructions"][adult_at:]
head = d["instructions"][:adult_at]
stripped = head.rstrip()
d["instructions"] = stripped + "\n" + c.STORY_ENGINE + head[len(stripped):] + adult_before
assert d["instructions"][d["instructions"].index("<adult_mode>"):] == adult_before
log.append("instructions: story_engine section added before (unchanged) adult section")

# ------------------------------------------------------------ metadata
d["version"] = "2.6-long-campaign-authority-growth-simulation-dialogue-canon-dmmode"
d["description"] = d["description"].replace("v2.5 long-campaign", "v2.6 long-campaign", 1)
d["designNotes"] += (
    "\n\nv2.6 Canon, DM Mode & story layer:\n"
    "- CORE_CANON_FIDELITY + WORLD CANON SHEET tracker + Type-Moon primer lore.\n"
    "- CORE_DM_MODE slimmed to summaries; 12 DM_MODE_* blocks auto-load/unload from the DM Mode tracker via 24 triggers; final-check line.\n"
    "- New trackers: WORLD GOALS (visible), FACTIONS & REPUTATION, ASCENDANT VIEWS (AI-only).\n"
    "- story_engine section in instructions; crossing rule (willing people + carried items). Departure timing stays the player's decision.\n"
    "- Adult-mode section and Sexual descriptor tracker unchanged."
)

(ROOT / "world.json").write_text(json.dumps(d, ensure_ascii=False, indent=4), encoding="utf-8")
print("\n".join(f"- {x}" for x in log))
