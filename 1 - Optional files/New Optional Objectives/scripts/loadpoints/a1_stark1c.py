# Generated by BehavEd
# ( "All heli, omega, altantis and mandarin objectives have been completed" )
setCurrentAct(1 )
# ( "All town center objectives should be show here." )
# ( "************************" )
# ( "Mark the Welcome Back From Omega as already played" )
setGameFlag("stark", 6, 1 )
# ( "This marks the entrance to stark2 as used" )
setGameFlag("stark", 2, 1 )
# ( "Mark the Welcome Back From Atlantis as already played" )
setGameFlag("stark", 7, 1 )
# ( "Stark_Obj20: Pym Helmet was found in Omega3" )
setGameFlag("conv_vars", 14, 1 )
# ( "Stark_Obj30: The decryption module has not be give to Vision and the player needs to talk to Black Widow to get it" )
setGameFlag("conv_vars", 5, 1 )
# ( "Stark_Obj40: The Ultimo Schematics was found in Mandarin and given to Fury" )
setGameFlag("conv_vars", 4, 1 )
# ( "Stark_Obj50: The player asked Pym to look at the data feed" )
getObjective("stark_obj50", "COMPLETE" )
# ( "Stark_Obj60:  The player hs found the cufflinks" )
setGameFlag("stark", 11, 1 )
objective ( "Stark_Obj10",  "EOBJCMD_SHOW" )
objective ( "Stark_Obj10",  "EOBJCMD_COMPLETE" )
objective ( "Stark_Obj20",  "EOBJCMD_SHOW" )
objective ( "Stark_Obj20",  "EOBJCMD_COMPLETE" )
objective ( "Stark_Obj30",  "EOBJCMD_SHOW" )
objective ( "Stark_Obj40",  "EOBJCMD_SHOW" )
objective ( "Stark_Obj50",  "EOBJCMD_SHOW" )
objective ( "Stark_Obj50",  "EOBJCMD_COMPLETE" )
objective ( "Stark_Obj60",  "EOBJCMD_SHOW" )
objective ( "Stark_Obj60",  "EOBJCMD_COMPLETE" )
objective ( "Stark_Obj70",  "EOBJCMD_SHOW" )
objective ( "Stark_Obj70",  "EOBJCMD_COMPLETE" )
# ( "The still need to be added..." )
# ( "************************" )
# ( "The following objectives show have already been completed" )
objective ( "Heli_Obj0",  "EOBJCMD_SHOW" )
objective ( "Heli_Obj10",  "EOBJCMD_SHOW" )
objective ( "Heli_Obj20",  "EOBJCMD_SHOW" )
objective ( "Heli_Obj30",  "EOBJCMD_SHOW" )
objective ( "Heli_Obj40",  "EOBJCMD_SHOW" )
# ( "This shows all of the omega objectives for stark1" )
objective ( "Omega_obj0",  "EOBJCMD_SHOW" )
objective ( "Omega_obj10",  "EOBJCMD_SHOW" )
objective ( "Omega_obj20",  "EOBJCMD_SHOW" )
objective ( "Omega_obj30",  "EOBJCMD_SHOW" )
objective ( "Omega_obj40",  "EOBJCMD_SHOW" )
# ( "Omega_Obj45 (epilogue): Save Omega database on the Legacy Virus from the Super Soldiers who are trying to destroy it." )
objective ( "Omega_obj45",  "EOBJCMD_SHOW" )
objective ( "Omega_obj50",  "EOBJCMD_SHOW" )
objective ( "Omega_obj60",  "EOBJCMD_SHOW" )
objective ( "Omega_obj70",  "EOBJCMD_SHOW" )
objective ( "Omega_obj80",  "EOBJCMD_SHOW" )
# ( "This shows all of the atlantis objectives for stark1" )
objective ( "Atlantis_Obj0",  "EOBJCMD_SHOW" )
objective ( "Atlantis_Obj10",  "EOBJCMD_SHOW" )
# ( "CSS: Atlantis_Obj20 doesn't exist" )
objective ( "Atlantis_Obj30",  "EOBJCMD_SHOW" )
# ( "Atlantis_Obj40 (epilogue): Gather Wakame seaweed in Atlantis3 to create a medicine that will heal Namor." )
objective ( "Atlantis_Obj40",  "EOBJCMD_SHOW" )
objective ( "Atlantis_Obj50",  "EOBJCMD_SHOW" )
objective ( "Atlantis_Obj60",  "EOBJCMD_SHOW" )
# ( "This shows all of the mandarin objectives for stark1" )
objective ( "Mandarin_Obj0",  "EOBJCMD_SHOW" )
objective ( "Mandarin_Obj10",  "EOBJCMD_SHOW" )
# ( "This completes all of the heli objectives" )
objective ( "Heli_Obj10",  "EOBJCMD_COMPLETE" )
objective ( "Heli_Obj20",  "EOBJCMD_COMPLETE" )
objective ( "Heli_Obj30",  "EOBJCMD_COMPLETE" )
objective ( "Heli_Obj40",  "EOBJCMD_COMPLETE" )
# ( "This completes all of the omega objectives" )
objective ( "Omega_obj10",  "EOBJCMD_COMPLETE" )
objective ( "Omega_obj20",  "EOBJCMD_COMPLETE" )
objective ( "Omega_obj30",  "EOBJCMD_COMPLETE" )
objective ( "Omega_obj40",  "EOBJCMD_COMPLETE" )
objective ( "Omega_obj45",  "EOBJCMD_COMPLETE" )
objective ( "Omega_obj50",  "EOBJCMD_COMPLETE" )
objective ( "Omega_obj60",  "EOBJCMD_COMPLETE" )
objective ( "Omega_obj70",  "EOBJCMD_COMPLETE" )
objective ( "Omega_obj80",  "EOBJCMD_COMPLETE" )
# ( "This completes all of the atlantis objectives" )
objective ( "Atlantis_Obj10",  "EOBJCMD_COMPLETE" )
objective ( "Atlantis_Obj30",  "EOBJCMD_COMPLETE" )
objective ( "Atlantis_Obj40",  "EOBJCMD_COMPLETE" )
objective ( "Atlantis_Obj50",  "EOBJCMD_COMPLETE" )
objective ( "Atlantis_Obj60",  "EOBJCMD_COMPLETE" )
# ( "This completes all of the mandarin objectives" )
objective ( "Mandarin_Obj10",  "EOBJCMD_COMPLETE" )
loadMap("act1/stark/stark1" )

