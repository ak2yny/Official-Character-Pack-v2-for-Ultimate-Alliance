# Generated by BehavEd
# ( "This script checks if the player has the gizmos" )
got_gizmos = getObjective("doomstark_obj40", "COMPLETE" )
if got_gizmos == 1
     # ( "This is where the damper is at" )
     setGameFlag("dstark", 5, 1 )
     # ( "There is where the manual" )
     setGameFlag("dstark", 6, 1 )
     # ( "8.	Player has ultimate weapon for the end fight" )
     setGameFlag("dstark", 8, 1 )
     # ( "Complete all objectives (fixes a bug)" )
     objective ( "doomstark_obj0",  "EOBJCMD_COMPLETE" )
     allowConversation("TRUE" )
else
     allowConversation("FALSE" )
endif

