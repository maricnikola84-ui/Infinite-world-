# v2.4 → v2.5 changes

`world.json` is the file to import. `world_original.json` is your untouched v2.4. Rebuild with `python3 tools/apply_v25.py`.

**Unchanged on purpose:** the adult-mode section, the Sexual descriptor tracker, all 18 trackers and their starting values, all 14 triggers, the character, background, summaryRequest and reply-length bands.

## Every edit
- hideSkillSystem=true, allowChangeCharacterSkills=false (SKILLS & TRAINING is the single skill owner)
- block DYNAMIC_COMBAT: start empty (COMBAT_START trigger loads it)
- block CORE_SKILLS: D100 only when a roll is supplied (matched evaluation contract)
- descriptionRequest: sensing -> pointers to CORE_SENSING/PERCEPTION
- descriptionRequest: removed 2nd copy of appearance rule
- descriptionRequest: dialogue duplicates -> pointer to VOICE_GATE/authorStyle
- evaluationRequest: knowledge_sensing duplicates -> pointer
- evaluationRequest: time_resources: removed fatigue repeat (owned by CORE_RESOURCE_RESOLUTION + hard rule)
- evaluationRequest: npc_world_motion: removed 2 repeats of the CORE_WORLD_MOTION prerequisite rule
- evaluationRequest: reference updated (NPC_DRIVES merged into NPC_BEHAVIOR)
- instructions: reference updated (NPC_DRIVES merged into NPC_BEHAVIOR)
- block CORE_VOICE_GATE: removed sentence duplicated inside the same block
- block CORE_NATURAL_SPEECH: removed quota repeat (owned by CORE_VOICE_GATE)
- block CORE_NATURAL_SPEECH: removed DM-mode repeat (owned by CORE_DM_MODE)
- block CORE_PARAMETERS: regen rank values -> pointer to CORE_TIME
- block CORE_NPC_BEHAVIOR: merged CORE_NPC_DRIVES drives list + pressure-not-compulsion rule
- block CORE_NPC_BEHAVIOR: role rule absorbs NPC_DRIVES nuance; offscreen repeat removed (owned by CORE_WORLD_MOTION)
- block CORE_NPC_DRIVES removed after merge into CORE_NPC_BEHAVIOR
- block CORE_MEMORY_LIFECYCLE: merged unique CORE_LONG_TERM_MEMORY rules; offscreen repeat removed
- block CORE_LONG_TERM_MEMORY removed after merge into CORE_MEMORY_LIFECYCLE (summary budget stays in summaryRequest)
- lore ETHER_LORE: regen table + time accounting -> pointer (kept unique cost guidance)
- lore ATTRIBUTE_SCALE_LORE: duplicate of CORE_PARAMETERS -> pointer + unique notation example
- lore SKILL_SYSTEM_LORE: perception/power/advancement repeats -> pointer (kept domain definitions)
- lore EARTH_LORE: continuity/reaction repeats -> pointer (kept public arc, memes, world-selection note)
- lore AHRIMAN_LORE: removed keywords ['whispers', 'malice', 'corruption']
- lore CHERNOBOG_LORE: removed keywords ['Forsaken', 'Forgotten', 'Forbidden', 'Frozen']
- lore TRAITS_LORE: removed keywords ['Campione']
- lore SKILL_SYSTEM_LORE: removed keywords ['Acrobatics', 'Arcana', 'Athletics', 'Crafting', 'Deception', 'Diplomacy', 'Intimidation', 'Medicine', 'Nature', 'Occultism', 'Performance', 'Religion', 'Society', 'Stealth', 'Survival', 'Thievery', 'teacher']
- lore ATTRIBUTE_SCALE_LORE: removed keywords ['E+', 'A+', 'S+']
- authorStyle: added style reference passage; fixed broken DM_MODE_LORE reference -> CORE_DM_MODE
- descriptionRequest: added viewpoint-mirroring rule
