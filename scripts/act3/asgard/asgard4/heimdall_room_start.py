# Generated by BehavEd
# ( "This starts the heimdall room stuff" )
startCutScene("FALSE", "FALSE" )
moveHeroesToEnt("herospot06" )
# ( "Using the relay to act on hdlockguy01 and hdlockguy02" )
cameraMove(" 298.420 3670.940 110.030 ", 1.000 )
cameraPan(" 0.000 40.000 270.000 ", 1.000, "FALSE" )
waittimed ( 1.500 )
copyOriginAndAngles("hd_door_clip", "hd_barrier_spot" )
# ( "Using the relay to act on hd_forcefield, heimdall_spawner, shocker_spawner, rhino_spawner" )
# ( "troll_spawner_hd01, and troll_spawner_hd02" )
act("hd_room_start_relay_2", "hd_room_start_relay_2" )
waittimed ( 1.000 )
playanim (  "EA_ZONE2", "heimdall", "LOOP", "" )
cameraMove(" 299.470 3925.220 341.490 ", 2.000 )
cameraPan(" 0.000 48.200 89.600 ", 2.000, "FALSE" )
waittimed ( 2.000 )
startCharConversation("act3/asgard/asgard4/3_ASGARD4_070", "hulk", "act3/asgard/asgard4/3_ASGARD4_082" )

