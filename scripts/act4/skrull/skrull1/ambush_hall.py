# Generated by BehavEd
# ( "Encounter with Skrulls" )
startCutScene("FALSE", "TRUE" )
heroNoTarget("TRUE" )
act("skrulla", "skrulla" )
act("skrullb", "skrullb" )
act("skrullc", "skrullc" )
act("skrulld", "skrulld" )
act("sklead", "sklead" )
# ( "Camera move" )
cameraFocusToEntity("wp_devilead01", 512.000, 45.000, 180.000, 1.000 )
# ( "Some time to get to waypoints" )
waittimed ( 5.000 )
# ( "Conversation" )
display ( "HELLO HUMANS! WE ARE GREEN PEOPLE" )
waittimed ( 1.000 )
# ( "Move this to a new Script, Punisher Bots break in" )
cameraFocusToEntity("wp_devilead01", 600.000, 80.000, 180.000, 1.000 )
waittimed ( 1.000 )
killEntity("win1" )
act("spwnr_1bot", "spwnr_1bot" )
waittimed ( 0.500 )
killEntity("win2" )
act("spwnr_2bot", "spwnr_2bot" )
waittimed ( 0.125 )
setWaypointPath("galactot1", "galactota", 1 )
setWaypointPath("galactot2", "galactotb", 1 )
waittimed ( 1.000 )
attackEntityWithType("galactot1", "c", "POWERSMASH", "FALSE" )
attackEntityWithType("galactot2", "d", "POWERSMASH", "FALSE" )
waittimed ( 2.000 )
endCutScene("FALSE", "TRUE" )
