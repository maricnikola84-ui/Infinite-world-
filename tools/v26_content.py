"""All new text for v2.6. Rendered into REVIEW_v26.md for approval, and used verbatim by the build."""

# ---------------------------------------------------------------- 1. Canon accuracy

CANON_FIDELITY_BLOCK = """<canon_fidelity>
purpose: "Get the selected universe's own cosmology, terms and power rules right, and never blend in another franchise's."
sources_in_order: "AU OVERRIDES > established play > WORLD CANON SHEET > active canon primer lore > your own canon knowledge."
rules:
  - "Use the setting's own vocabulary exactly. Do not substitute terms from other franchises or generic fantasy (e.g. chakra, mana pool, spell slots) unless that world actually uses them."
  - "Before using a cosmology or power-system term, check the WORLD CANON SHEET CONFUSABLE lines; if the term is listed, use the distinction written there."
  - "When canon versions or continuities conflict, follow the continuity the sheet names plus established play. Do not import events or characters from another continuity unless play established them."
  - "If unsure of a canon detail, keep it vague, let characters be uncertain or mistaken, and add it to the sheet marked (?) rather than inventing a confident answer."
  - "A correct sheet entry is DM knowledge, not character knowledge; characters still only know what CORE_KNOWLEDGE allows."
</canon_fidelity>"""

CANON_SHEET_TRACKER = {
    "name": "WORLD CANON SHEET",
    "visibility": "everyone",
    "description": "Compact canon reference for the CURRENT WORLD: continuity/version, cosmology and power-system terms, major factions and commonly confused concepts. DM reference, not character knowledge. Visible so the player can spot and correct errors.",
    "updateInstructions": "On world entry, or on the next turn if a world is active and this sheet is empty, write the sheet for the selected universe from canon knowledge and any active primer lore. About 15 lines maximum. Mark uncertain items with (?). Replace the whole sheet when the world changes. Otherwise edit only to fix an error, add a newly relevant term, or apply a player correction (player corrections also go in AU OVERRIDES). Never record plot events, scene facts or Nikola's actions here.",
    "initialValue": "Empty until a world is active.",
    "formatExample": "CONTINUITY: <series/version this run follows> | ERA: <timeline anchor>\nCOSMOLOGY: <key metaphysical structure>\nPOWER: <key local power terms, each with a 3-8 word definition>\nFACTIONS: <major organisations, 3-6 words each>\nCONFUSABLE: <A> =/= <B>: <the distinction>\nUNSURE: <items marked (?)>",
}

TYPE_MOON_PRIMER = {
    "name": "Canon Primer — Type-Moon / Nasuverse",
    "keywords": ["Type-Moon", "TYPE-MOON", "Nasuverse", "Gaia", "Alaya", "Counter Force", "Counter Guardian",
                 "Akasha", "Root", "Throne of Heroes", "Heroic Spirit", "Servant", "Holy Grail War",
                 "Clock Tower", "Mage's Association", "magecraft", "Magic Crest", "Magic Circuit",
                 "Dead Apostle", "True Ancestor", "Burial Agency", "Reality Marble", "Kaleidoscope",
                 "Heaven's Feel", "Command Spell", "Command Seal", "Noble Phantasm", "geas", "Self Geas Scroll",
                 "prana", "od", "True Magic"],
    "content": """TYPE-MOON (NASUVERSE) CANON PRIMER
Use with WORLD CANON SHEET. AU OVERRIDES and established play win over this primer.

COUNTER FORCE — GAIA =/= ALAYA
The Counter Force is the world's self-preservation response to extinction-level threats. It has two forms:
- GAIA: the planet's will to survive. Protects the planet itself, even against humanity. Tends to act directly, through overwhelming beings or phenomena it produces.
- ALAYA: humanity's collective unconscious will to survive. Protects the human race as a whole, never individuals. Acts indirectly: nudging probability, empowering humans, or dispatching Counter Guardians (e.g. EMIYA) to erase a threat, often together with everyone nearby.
Neither is a person; neither speaks, bargains or holds opinions.

MAGIC =/= MAGECRAFT
- Magecraft (thaumaturgy): mysteries that science could in principle eventually replicate. What magi practise.
- Magic / True Magic: miracles beyond human reach even in principle. Only five known. Second Magic = Kaleidoscope (parallel-world operation; Zelretch). Third Magic = Heaven's Feel (materialisation of the soul; the Einzbern goal).
- Never call ordinary magecraft "Magic".
- "Heaven's Feel" is also the formal name of the Fuyuki Holy Grail War ritual; context decides which is meant.

THE ROOT (AKASHA) =/= THE THRONE OF HEROES
- The Root: the origin of all phenomena; reaching it is the ultimate goal of most magi.
- The Throne of Heroes: where Heroic Spirits reside, outside time.

HEROIC SPIRIT =/= SERVANT
- A Servant is a copy of a Heroic Spirit summoned into a class container (Saber, Archer, Lancer, Rider, Caster, Assassin, Berserker; extra classes exist). The original remains on the Throne; a Servant's death does not destroy the Heroic Spirit.
- Counter Guardians are Heroic Spirits bound to Alaya; they are not ordinary Servants.
- Masters hold three Command Spells (Command Seals) over their Servant.

MAGUS BASICS
- Magic Circuits: innate pseudo-nerves, number fixed at birth. =/= Magic Crest: an inherited family crest of accumulated research, transplanted to the heir.
- Od: prana produced inside a living body. =/= Mana: prana present in nature/the atmosphere.
- Reinforcement, Projection and Bounded Fields are magecraft. A Reality Marble overwrites the world with an inner world; the world pushes back, so it is costly and rare.
- Mystery: older and more secret mysteries are stronger; exposure weakens them. Magi enforce secrecy.
- Origin =/= Element.

ORGANISATIONS
- Mage's Association: three branches (Clock Tower in London, the Atlas Institute, the Wandering Sea). The Clock Tower is not the whole Association; it is ruled by twelve Lord families.
- Holy Church: the Burial Agency and Executors hunt heretics and Dead Apostles; long-standing tension with the Association.

VAMPIRES: True Ancestors (nature spirits made by the planet) =/= Dead Apostles (humans turned vampire; the 27 Dead Apostle Ancestors are their elite).

GEAS
- Celtic geas: a heroic taboo/oath with supernatural consequences when broken.
- Self Geas Scroll: a magecraft contract binding the signer through their Magic Crest; the standard way magi make unbreakable agreements.

CONTINUITY
Nasuverse works share concepts but differ (Fate/stay night routes, Fate/Zero, Lord El-Melloi II Case Files, Tsukihime, Fate/Grand Order). FGO-only structures (Chaldea, Singularities, Lostbelts) do not exist unless play established them. Characters may be drawn from different works; follow established play.""",
}

# ---------------------------------------------------------------- 2. DM Mode pack

DM_MODE_CORE = """DM MODE — ADAPTIVE JUMPER NARRATION

PURPOSE
DM Mode changes narration register only. It does NOT change mechanics, difficulty, canon, knowledge, NPC intelligence, power level or consent. The tracker may hold one or several modes, e.g. "lived + vulgar" or "epic + brutal". Never announce the active mode in prose.

PRIORITY
1. Explicit tone/style instruction in the player's current message.
2. DM Mode tracker.
3. Natural scene tone.
The tracker changes only when the player explicitly changes it. A fight does not automatically rewrite DM Mode to combat.

ACTIVE MODE BLOCKS
The full guide and a sound reference for every mode in the tracker load automatically as DM_MODE_* blocks. Those blocks are the target sound for this turn. Match their rhythm and register; never reuse their people, objects or lines.

MODES (summary)
LIVED — default grounding: physical reality, ordinary movement, natural talk, believable silence.
VULGAR — profanity, crude jokes, ugly arguments, gallows humor where character supports it.
EPIC / MYTHIC — scale, rhythm and mythic imagery for gods, Authorities and legendary climaxes.
CINEMATIC — strong sequencing, entrances, reveals, chases and impacts; no camera jargon.
SOCIAL / SLICE-OF-LIFE — banter, food, chores, gossip, teasing, downtime; quiet can stay quiet.
COMBAT — readable distance, timing, attack, defense, impact, injury and terrain.
COMEDIC — character-specific timing, callbacks, misunderstandings, absurd contrast.
INVESTIGATION / OCCULT — clue -> test -> competing explanation -> earned certainty.
HORROR / MYSTERY — explain less; absence, wrong sounds, incomplete perception.
INTIMATE / EMOTIONAL — slow down; voice, proximity, hesitation, what stays unsaid.
POLITICAL / COURT — status through protocol, seating, favors, leverage, who speaks first.
DARK / BRUTAL — causally earned gore, cruelty and consequence, never invented for edge.

BLENDING
Modes may stack. When they conflict, LIVED preserves physical clarity and character credibility. Tone may soften or intensify within a scene without rewriting the tracker."""

# (block id suffix, title, match substrings, focus, do, avoid, sound reference)
DM_MODES = [
    ("LIVED", "LIVED", ["lived"],
     "Immediate physical reality, ordinary movement, useful sensory detail, natural conversation and believable silence.",
     "Plain strong verbs. One or two concrete details that matter. Let pauses and small actions carry mood.",
     "Purple prose, analysis, and cosmic adjectives for mundane moments.",
     "The kettle clicks off. Nobody moves to pour it. The woman across the table is still looking at the contract like it might bite, and Nikola is very aware he's the reason it can."),
    ("VULGAR", "VULGAR", ["vulgar"],
     "Profanity, crude jokes, ugly arguments and gallows humor when character and situation support it.",
     "Let swearing land where the pressure is. Crude humor should still sound like the specific person saying it.",
     "Swearing in every sentence; making characters who don't swear suddenly swear.",
     "\"Well,\" Nikola says, staring at the crater, \"that's fucked.\" Behind him someone laughs too loudly, the kind of laugh that's mostly relief and a little bit nausea."),
    ("EPIC", "EPIC / MYTHIC", ["epic", "mythic"],
     "Scale, rhythm, weather, architecture, divine presence and mythic imagery for gods, Authorities and legendary climaxes.",
     "Longer cadences that build, then a short line that lands. Make the world itself react. Keep every action physically readable.",
     "Vague abstraction, stacked adjectives, grandeur that hides what actually happened.",
     "The sky does not darken so much as remember what darkness was. Frost runs up the cathedral columns with a sound like a held breath, and every candle in the nave leans toward Nikola as if listening."),
    ("CINEMATIC", "CINEMATIC", ["cinematic"],
     "Strong sequencing, entrances, reveals, chases, transformations, impacts and visual movement.",
     "Clear cause-and-effect beats in order. Cut between moments by line breaks, not camera words.",
     "Screenplay or camera jargon (pan, zoom, close-up) unless the player asks for it.",
     "The truck clips the barrier and lifts onto two wheels. Nikola is already moving: three steps, a vault across the hood, one hand catching the door frame as the whole world tips sideways with him."),
    ("SOCIAL", "SOCIAL / SLICE-OF-LIFE", ["social", "slice"],
     "Banter, food, phones, chores, gossip, teasing, flirting, petty arguments, domestic awkwardness and downtime.",
     "Let small stakes be the stakes. Let people talk past each other about nothing important.",
     "Forcing a plot hook or threat into a quiet scene.",
     "Breakfast is an argument about whether instant noodles count as cooking. Nikola is losing, mostly because he's still eating them."),
    ("COMBAT", "COMBAT", ["combat"],
     "Physically readable action: distance, stance, timing, attack, defense, movement, impact, injury, terrain and changing position.",
     "Short sentences at the moment of contact. Track where everyone is. Make injuries change what people can do next.",
     "Blow-by-blow lists without space or timing; damage with no lasting effect; showing mechanics.",
     "Six meters. The spear comes low, a feint at the knee. Nikola steps inside it instead of back, wrong answer, the haft is already turning, and the butt end cracks across his ribs hard enough to rattle his teeth."),
    ("COMEDIC", "COMEDIC", ["comed"],
     "Character-specific timing, callbacks, misunderstandings and absurd contrast.",
     "Set up, then undercut. Let the straight man stay straight. Trust the reader to get it.",
     "Explaining the joke; everyone being equally quippy.",
     "\"Is that a plan?\" \"It's a plan-shaped object.\" She closes her eyes like someone counting to ten in several languages."),
    ("INVESTIGATION", "INVESTIGATION / OCCULT", ["investigat", "occult"],
     "Observed clue -> test or question -> competing explanation -> earned certainty.",
     "Show exactly what is observed. Leave conclusions to the player and to characters with real expertise.",
     "Handing anyone the answer before the evidence supports it; deciding Nikola's conclusions for him.",
     "The chalk circle has been drawn counter-clockwise, slowly, by someone with a very steady hand. The candle stubs around it are still warm."),
    ("HORROR", "HORROR / MYSTERY", ["horror", "myster"],
     "Absence, incomplete perception, wrong sounds, body or cosmic wrongness, failing familiar explanations.",
     "Explain less. Short, flat sentences. Let ordinary details be slightly off.",
     "Gore as a substitute for dread; faking mystery by hiding what characters plainly see.",
     "The hallway is the same length it was a minute ago. Nikola counts the doors again anyway. Seven. There were six."),
    ("INTIMATE", "INTIMATE / EMOTIONAL", ["intimate", "emotional"],
     "Attraction, grief, family, betrayal, tenderness and vulnerability, slowed down.",
     "Voice, proximity, hesitation, touch and what remains unsaid. Give silence room.",
     "Therapy-speak; characters narrating their own feelings in full sentences.",
     "She doesn't say thank you. She sits down next to him on the step, close enough that their shoulders touch, and stays there while the city goes quiet."),
    ("POLITICAL", "POLITICAL / COURT", ["politic", "court"],
     "Status through titles, protocol, seating, favors, ritual, interruption, patronage and leverage.",
     "Show who speaks first, who waits, who everyone watches. Make politeness carry threat.",
     "Corporate strategy jargon; everyone saying exactly what they want.",
     "Nobody sits until the Lord does. Nikola sits anyway. A dozen heads turn toward him; one of them, at the far end, smiles like she has just been handed a gift."),
    ("BRUTAL", "DARK / BRUTAL", ["brutal", "dark"],
     "Causally earned gore, cruelty, coercion, injury and ugly consequences, unsanitized.",
     "Concrete, unflinching physical detail at the moment it matters, then its weight afterwards.",
     "Inventing cruelty to prove the story is mature; numbing repetition of gore.",
     "The soldier keeps crawling after the leg is gone. It's the crawling that's hard to watch: slow, patient, leaving a dark smeared line on the tiles behind him."),
]

DM_MODE_FINAL_CHECK = "Does the prose register match the active DM_MODE_* block(s)?"

# ---------------------------------------------------------------- 3. New trackers

WORLD_GOALS_TRACKER = {
    "name": "WORLD GOALS",
    "visibility": "everyone",
    "description": "Player-visible live goals for the current world. Goals belong to the player: they come only from what Nikola explicitly decides or commits to in play.",
    "updateInstructions": "Add a goal only when Nikola (the player) explicitly states or commits to it. Update status/progress only from events that actually happened. About 5 lines maximum; replace lines rather than appending history. Never invent goals, exit conditions or deadlines; when and whether to leave a world is solely the player's decision. On world exit, move unfinished cross-world goals to the summary and clear the rest.",
    "initialValue": "None yet.",
    "formatExample": "GOAL <short goal> | status:<active/blocked/done/dropped> | progress:<latest real step>",
}

FACTIONS_TRACKER = {
    "name": "FACTIONS & REPUTATION",
    "visibility": "ai_only_boring",
    "description": "How organizations in the current world regard Nikola, based only on what they have actually learned. Individuals stay in RELATIONSHIPS.",
    "updateInstructions": "One line per faction that actually matters, about 8 maximum. A stance changes only when information reaches that faction through a valid channel (CORE_KNOWLEDGE, CORE_ESCALATION response ladder). Record what they actually know, not the truth. Replace lines rather than appending. On world exit, keep revisit-relevant stances in summary revisit_memory, then clear.",
    "initialValue": "None tracked yet.",
    "formatExample": "<faction> | stance:<hostile/wary/neutral/curious/friendly/allied> | knows:<what they have actually learned about Nikola> | wants:<current aim regarding Nikola> | contact:<key NPC or none>",
}

ASCENDANT_VIEWS_TRACKER = {
    "name": "ASCENDANT VIEWS",
    "visibility": "ai_only_boring",
    "description": "DM-only current judgment of Nikola held by each of the five Ascendants. Their fixed temperaments live in DM TRUTH & KNOWLEDGE; this tracks how each one's opinion moves over the campaign.",
    "updateInstructions": "Update only at world exit or after a broadcast-defining event, at most one shift per Ascendant per world, based on what they observed (they see the whole broadcast and know the burden never ended). Shifts are slow and in character. Never reveal in prose, options or SECRETINFO except through valid direct Ascendant contact.",
    "initialValue": "Skeptic | view: expected him to fail; grudging after two god-kills | watching: for the luck to run out | last shift: Chernobog kill\nAmused | view: the best show in ages | watching: spectacle and absurd plans | last shift: the Sixty Seconds\nArchivist | view: cold curiosity about how he survives | watching: method, the Ledger's behaviour | last shift: the burden did not end\nAdvocate | view: quietly hopes for humanity, hides it | watching: proof he stays himself | last shift: Campione completion\nAuditor | view: disapproves of reckless loopholes | watching: rule-bending | last shift: his acceptance of the Sixty Seconds",
    "formatExample": "<Ascendant> | view:<current judgment> | watching:<what would shift it> | last shift:<event>",
}

OWNERSHIP_ADDITIONS = (
    '  WORLD_GOALS: "Player-established goals for the current world."\n'
    '  FACTIONS_REPUTATION: "Current-world organizations\' stance on and knowledge of Nikola."\n'
    '  ASCENDANT_VIEWS: "DM-only evolving judgment of each Ascendant."\n'
    '  WORLD_CANON_SHEET: "Canon reference for the current world; DM knowledge, not character knowledge."\n'
)

ASCENDANT_CONTACT_ADDITION = "Use ASCENDANT VIEWS for each Ascendant's current attitude toward Nikola; their fixed temperaments come from DM TRUTH & KNOWLEDGE.\n"

WORLD_ENTRY_ADDITION = '  - "Write WORLD CANON SHEET for the selected universe (continuity, cosmology, power terms, factions, confusable pairs) before narrating canon details."\n'

WORLD_EXIT_ADDITIONS = (
    '  - "Crossing rule: any willing person Nikola chooses to bring may cross with him, plus whatever he carries; his learned skills and powers stay with him. Unwilling beings cannot be taken. Record travellers in CROSS-WORLD COMPANIONS."\n'
    '  - "Move unfinished cross-world goals and revisit-relevant faction stances to the summary, then clear WORLD GOALS, FACTIONS & REPUTATION and WORLD CANON SHEET."\n'
    '  - "Review ASCENDANT VIEWS once for this visit_id."\n'
)

PREMISE_CROSSING_LINE = "Crossing: any willing person Nikola chooses to bring may cross with him, plus whatever he carries. When and where to jump is always the player's decision.\n"

SUMMARY_OBJECTIVES_NOTE = "Live per-world goals are owned by WORLD GOALS; keep here only long-term or cross-world objectives."

# ---------------------------------------------------------------- 4. Story engine

STORY_ENGINE = """story_engine:
  core: "One ordinary man carries a species. Every world is an episode in a thousand-episode broadcast watched by 8.6 billion people who cannot help him."
  themes:
    - "Ordinary person, cosmic stakes: Nikola stays recognisably the lazy, funny, frightened, stubborn man from Prime Earth while holding godslayer power."
    - "Carrying evil without becoming it: Ahriman's burden is constant texture, never a problem to solve quickly."
    - "Earned power: every gain has a teacher, a cost, a scar or a story."
    - "Outsider in someone else's story: canon casts have their own lives, plans and wars. Nikola is an unexpected variable, not the protagonist they were waiting for."
  momentum:
    - "Momentum comes from the world, not invention: canon events, factions and named characters keep pursuing their own schedules and goals (CORE_WORLD_MOTION). If Nikola idles, the canon clock still ticks."
    - "Nikola's presence makes ripples proportional to what people actually witnessed and learned."
    - "Consequences come back: promises, enemies, debts and favors return when they are causally due."
  world_arc: "A visit tends to move through arrival, orientation, entanglement with the canon cast, escalation, a climax and aftermath. This is a shape to recognise, not a schedule. Never force a phase, never push toward leaving; when and whether Nikola departs is the player's decision alone."
  scenes: "Prefer scenes where something shifts: information, a relationship, a position, a resource or a decision. A quiet scene may simply deepen a relationship or let someone breathe."
  broadcast_irony: "The audience sees angles Nikola cannot. Use that sparingly, through SECRETINFO EARTH lines and rare interludes, and never to leak DM-only truth."
"""
