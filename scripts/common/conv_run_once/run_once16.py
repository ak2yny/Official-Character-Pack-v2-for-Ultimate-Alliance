# Generated by BehavEd
# ( "conv_vars is also 0, if the player didn't give a passwort or start the quest - this is a bug - fixed by adding new flag" )
# ( "If this is set to 1, then the player gave the wrong password" )
pwd_wrong = getGameFlag("opt_obj", 1 )
if pwd_wrong == 1
     # ( "This makes sure that the start condition is run only once" )
     allowConversation("TRUE" )
else
     allowConversation("FALSE" )
endif
