###---how to load different eyes---###
happy_eyes = ImageFile.LOVE 
norm_eyes = ImageFile.NEUTRAL

ev3.screen.load_image(happy_eyes)
ev3.screen.load_image(norm_eyes)

###---how to make different sounds---###
ev3.speaker.play_file(SoundFile.DOG_GROWL)

###---how to move its head---###
head_motor = Motor(Port.B, Direction.COUNTERCLOCKWISE,
                                gears=[[1, 24], [12, 36]])
head_motor.run(3000)
head_motor.run(-3000)
