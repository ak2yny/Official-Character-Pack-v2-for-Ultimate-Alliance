# Generated by BehavEd
setRecallActive("FALSE" )
# ( "Unneeded ents... until I spawn them specifically" )
remove ( "fallball", "fallball" )
remove ( "pinball1", "pinball1" )
remove ( "THEFURY", "THEFURY" )
remove ( "THEPAIN", "THEPAIN" )
# ( "MEOW!... um, I mean: Play Conversation if this is the first time here." )
firsties = getGameFlag("murder3", 3 )
if firsties == 0
     setGameFlag("murder3", 3, 1 )
     Sabretooth = isActorOnTeam("Sabretooth" )
     if Sabretooth == 1
	startConversation("act2/murder/murder3/2_murder3_012_DLC" ) 
     else
	startCharConversation("act2/murder/murder3/2_murder3_010", "mrfantastic", "act2/murder/murder3/2_murder3_012" )
     endif
endif
# ( "has 1,000,000 points been reached already?" )
check = getGameFlag("murder3", 6 )
if check == 1
     # ( "1,000,000 points has been reached--destroy flippers" )
     remove ( "pushend1", "pushend1" )
     remove ( "pushend2", "pushend2" )
     killEntitySilent("flipperend1" )
     killEntitySilent("flipperend2" )
     remove ( "dclip_flippers", "dclip_flippers" )
     setEnable("ball_trigger", "TRUE" )
endif
# ( "has the golden ticket been found already?" )
check = getGameFlag("m2_tickets", 1 )
if check == 1
     # ( "the golden ticket has been found--remove ticket; prepare exit" )
     remove ( "gold_ticket", "gold_ticket" )
     actSilent("exit_gate", "exit_gate" )
     setEnable("link_murder2", "TRUE" )
endif
# ( "has rhino_block been lowered already?" )
check = getGameFlag("murder3", 4 )
if check == 1
     # ( "yes--make sure it starts lowered; clean up relay" )
     actSilent("rhino_block", "rhino_block" )
     remove ( "relay_rhino_block", "relay_rhino_block" )
endif
# ( "has shock_block been lowered already?" )
check = getGameFlag("murder3", 5 )
if check == 1
     # ( "yes--make sure it starts lowered; clean up relay" )
     actSilent("shock_block", "shock_block" )
     remove ( "relay_shock_block", "relay_shock_block" )
endif

