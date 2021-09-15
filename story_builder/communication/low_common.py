from .communication import Communication

class LowCommon(Communication):

    def greeting(self):
        return self.randomizer([
            "Hey, what's up?",
            "Yo Yo Yo, hey there home-slice!",
            "Eh, sup?",
            "What's happinin'?",
            "DUDE! How're you doin?",
        ])

    def challenge(self):
        return self.randomizer([
            "Dude, you trippin!",
            "Boy/Girl, you dun f'd up!",
            "That's it, time to throw down!",
        ])

    def taunt(self):
        return self.randomizer([
            "Ya ready to get ya Ass whoooooped?!",
            "You must be dumber than a box of.... dummies!",
            "I bet I gots more teeth than you gots brains!",
            "Yo momma so ugly, even my drunk cuzin Reggie wouldn't kiss her!",
        ])

    def announce_presense(self):
        return self.randomizer([
            "HEY YALL!",
            "HEY OH!  LET'S PARTY!",
            "YO YO YO, I HAVE ARRIVED!",
            "SUP BITCHES!",
        ])

    def question_presense(self):
        if self.hostile():
            output = self.randomizer([
                "Who da hell are you?",
            ])
        elif self.unfriendly():
            output = self.randomizer([
                "What'd you want?",
            ])
        elif self.friendly() or self.fake():
            output = self.randomizer([
                "Are you in da right place?",
            ])
        
        return output

    def haggle_lower(self):
        return self.randomizer([
            "Man, you must be crazy!",
            "Momma didn't raise no dummy! I ain't payin that!",
            "Shooooot! Boy/Girl that theres worth fightin over!",
        ])

    def haggle_higher(self):
        return self.randomizer([
            "Even your momma charges more than that!",
            "I betcha I could sell MY liver for more than that!",
            "Get your head right! Thas a weak ass offer!",
        ])

    def flatter(self):
        return self.randomizer([
            "You're prettier than my second cousin!",
            "You have a purdy mouth!",
            "You got some nice child bearin hips!",
            "You sure are good at.... things!",
        ])

    def admire(self):
        return self.randomizer([
            "I sure wish I had as many teeth as you!",
            "I think you might just be da smartest person I knows!",
            "That's even better than my mommas home-made baby-bourbon!",
        ])

    def admonish(self):
        return self.randomizer([
            "Shiiiiitttt, you must have dung for brains!",
            "Dude, even I wouldn't do that.....and I would do lots of stuff!",
            "You's a big 'ol dummy!",

        ])

    def encourage(self):
        return self.randomizer([
            "You can do it, ALL NIGHT LONG!!"
        ])

    
