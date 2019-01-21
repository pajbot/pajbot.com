class Sample:
    def __init__(self, command, link, date_added=''):
        self.command = command
        self.link = link
        self.date_added = date_added

    def __lt__(self, other):
        return self.command < other.command

    def jsonify(self):
        return {
                'command': self.command,
                'link': self.link,
                'date_added': self.date_added,
                }

class ProcessedSample:
    def __init__(self, sample):
        self.command = sample.command
        self.samples = [sample]

    def __lt__(self, other):
        return self.command < other.command

    def add_sample(self, sample):
        self.samples.append(sample)

    def jsonify(self):
        return {
                'command': self.command,
                'samples': self.samples,
                }

playsound_samples = [
    Sample('bossofthisgym', 'http://soundboard.ass-we-can.com/static/music/MarkW/Boss of this gym.mp3'),
    Sample('fuckyou', 'http://soundboard.ass-we-can.com/static/music/VanD/FUCKYOU.mp3'),
    Sample('idontdoanal', 'https://pajlada.se/files/clr/i_dont_do_anal.mp3'),
    Sample('knock', 'https://pajlada.se/files/clr/knock.mp3'),
    Sample('slap', 'https://pajlada.se/files/clr/slap.mp3'),
    Sample('cumming', 'https://pajlada.se/files/clr/cumming.mp3'),
    Sample('collegeboy', 'http://soundboard.ass-we-can.com/static/music/BillyH/Come%20on%20college%20boy.mp3'),
    Sample('oooh', 'https://pajlada.se/files/clr/oooh.mp3'),
    Sample('suction', 'https://pajlada.se/files/clr/suction.mp3'),
    Sample('takeit', 'http://soundboard.ass-we-can.com/static/music/VanD/Take%20it%20boy.mp3'),
    Sample('amazing', 'http://soundboard.ass-we-can.com/static/music/VanD/That\'s%20amazing.mp3'),
    Sample('power', 'https://pajlada.se/files/clr/power.mp3'),
    Sample('othernight', 'https://pajlada.se/files/clr/othernight.mp3'),
    Sample('asswecan', 'https://pajlada.se/files/clr/ass_we_can.mp3'),
    Sample('lashofthespanking', 'http://soundboard.ass-we-can.com/static/music/BillyH/Lash%20of%20the%20spanking.mp3'),
    # Sample('nyanpass', 'https://pajlada.se/files/clr/nyanpass.ogg'),
    Sample('scamazishere', 'https://pajlada.se/files/clr/scamaz_is_here.mp3'),
    Sample('lul', 'https://pajlada.se/files/clr/LUL.mp3'),
    Sample('ohmyshoulder', 'https://pajlada.se/files/clr/ohmyshoulder.mp3'),
    # Sample('tuturu', 'https://pajlada.se/files/clr/tuturu.mp3'),
    Sample('attention', 'https://pajlada.se/files/clr/attention.mp3'),
    Sample('aaaah', 'https://pajlada.se/files/clr/AAAAAAAH.mp3'),
    Sample('jesse', 'https://pajlada.se/files/clr/jesse-cook.mp3'),
    Sample('shakalaka', 'https://pajlada.se/files/clr/shakalaka.mp3'),
    Sample('loan', 'https://pajlada.se/files/clr/its_a_loan.mp3'),
    Sample('spankmoan1', 'https://pajlada.se/files/clr/spankmoan1.mp3'),
    Sample('youlikechallenges', 'https://pajlada.se/files/clr/you_like_challenges.mp3'),
    Sample('youlikethat', 'https://pajlada.se/files/clr/you_like_that.mp3'),
    Sample('pants', 'https://pajlada.se/files/clr/ripped_pants.mp3'),
    # Sample('oh', 'https://pajlada.se/files/clr/oh.mp3'),
    # Sample('poi', 'https://pajlada.se/files/clr/poi.mp3'),
    # Sample('ayaya', 'https://pajlada.se/files/clr/ayaya.mp3'),
    Sample('car', 'https://pajlada.se/files/clr/car.mp3'),
    Sample('dayum', 'https://pajlada.se/files/clr/dayum.mp3'),
    Sample('water', 'https://pajlada.se/files/clr/water1.mp3'),
    Sample('doitdad', 'https://pajlada.se/files/clr/do_it_dad.mp3'),
    Sample('face', 'https://pajlada.se/files/clr/me_go_face.mp3'),
    Sample('sike', 'https://pajlada.se/files/clr/sike.mp3'),
    # Sample('yahallo', 'https://pajlada.se/files/clr/yahallo.mp3'),
    Sample('djkarlthedog', 'https://pajlada.se/files/clr/djkarlthedog.mp3'),
    Sample('bomblobber', 'https://pajlada.se/files/clr/bomb_lobber.mp3'),
    # Sample('baka', 'https://pajlada.se/files/clr/baka.mp3'),
    Sample('march', 'https://pajlada.se/files/clr/march.mp3'),
    Sample('embarrassing', 'https://pajlada.se/files/clr/embarrassing.mp3'),
    Sample('yessir', 'https://pajlada.se/files/clr/yes_sir.mp3'),
    Sample('sixhotloads', 'https://pajlada.se/files/clr/six_hot_loads.mp3'),
    Sample('wrongnumba', 'https://pajlada.se/files/clr/wrong_numba.mp3'),
    Sample('sorry', 'https://pajlada.se/files/clr/sorry.mp3'),
    Sample('relax', 'https://pajlada.se/files/clr/relax.mp3'),
    Sample('vibrate', 'https://pajlada.se/files/clr/vibrate.mp3'),

    Sample('4head', 'https://pajlada.se/files/clr/4Head.mp3'),
    # Sample('akarin', 'https://pajlada.se/files/clr/akarin.mp3'),
    Sample('behindyou', 'https://pajlada.se/files/clr/behindyou.mp3'),
    Sample('bitch', 'https://pajlada.se/files/clr/bitch.mp3'),
    Sample('damnson', 'https://pajlada.se/files/clr/damnson.mp3'),
    # Sample('desu', 'https://pajlada.se/files/clr/desu.mp3'),
    Sample('fatcock', 'https://pajlada.se/files/clr/fatcock.mp3'),
    Sample('gangingup', 'https://pajlada.se/files/clr/gangingup.mp3'),
    Sample('iseeyou1', 'https://pajlada.se/files/clr/iseeyou1.mp3'),
    Sample('iseeyou2', 'https://pajlada.se/files/clr/iseeyou2.mp3'),
    Sample('jeff', 'https://pajlada.se/files/clr/jeff.mp3'),
    Sample('mistake', 'https://pajlada.se/files/clr/mistake.mp3'),
    Sample('ohbabyatriple', 'https://pajlada.se/files/clr/ohbabyatriple.mp3'),
    # Sample('rin', 'https://pajlada.se/files/clr/rin.mp3'),
    Sample('sheeeit', 'https://pajlada.se/files/clr/sheeeit.mp3'),
    Sample('spook', 'https://pajlada.se/files/clr/spook.mp3'),
    Sample('surprise', 'https://pajlada.se/files/clr/surprise.mp3'),
    Sample('tuckfrump', 'https://pajlada.se/files/clr/tuckfrump.mp3'),
    # Sample('uguu', 'https://pajlada.se/files/clr/uguu.mp3'),
    Sample('weed', 'https://pajlada.se/files/clr/weed.mp3'),
    Sample('wrongdoor', 'https://pajlada.se/files/clr/wrongdoor.mp3'),

    # Sample('ryuu', 'https://pajlada.se/files/clr/hanzo.mp3'),

    Sample('yeehaw', 'https://pajlada.se/files/clr/yeehaw.mp3'),

    Sample('4header', 'https://pajlada.se/files/clr/4header.ogg'),
    Sample('athene', 'https://pajlada.se/files/clr/athene.ogg'),
    Sample('beatme123', 'https://pajlada.se/files/clr/beatme123.ogg'),
    Sample('bondagegaywebsite', 'https://pajlada.se/files/clr/bondagegaywebsite.ogg'),
    Sample('bubble', 'https://pajlada.se/files/clr/bubble.ogg'),
    Sample('celebrate', 'https://pajlada.se/files/clr/celebrate.ogg'),
    Sample('comeonletsgo', 'https://pajlada.se/files/clr/comeonletsgo.ogg'),
    Sample('gamba', 'https://pajlada.se/files/clr/gamba.ogg'),
    Sample('goodvibes', 'https://pajlada.se/files/clr/goodvibes.ogg'),
    Sample('heftobemad', 'https://pajlada.se/files/clr/heftobemad.ogg'),
    Sample('heyguyshowsitgoinkripparrianhere', 'https://pajlada.se/files/clr/heyguyshowsitgoinkripparrianhere.ogg'),
    Sample('jabroni', 'https://pajlada.se/files/clr/jabroni.ogg'),
    Sample('legendary', 'https://pajlada.se/files/clr/legendary.ogg'),
    Sample('mysummercmonman', 'https://pajlada.se/files/clr/mysummercmonman.ogg'),
    Sample('no', 'https://pajlada.se/files/clr/no.ogg'),
    Sample('nothinghere', 'https://pajlada.se/files/clr/nothinghere.ogg'),
    Sample('ohmancmonman', 'https://pajlada.se/files/clr/ohmancmonman.ogg'),
    Sample('oooooh', 'https://pajlada.se/files/clr/oooooh.ogg'),
    Sample('pain1', 'https://pajlada.se/files/clr/pain1.ogg'),
    Sample('pullupourpants', 'https://pajlada.se/files/clr/pants.ogg'),
    Sample('pleaseno', 'https://pajlada.se/files/clr/pleaseno.ogg'),
    Sample('powerfuck', 'https://pajlada.se/files/clr/powerfuck.ogg'),
    Sample('puke', 'https://pajlada.se/files/clr/puke.ogg'),
    Sample('reynad', 'https://pajlada.se/files/clr/reynad.ogg'),
    Sample('righthappy', 'https://pajlada.se/files/clr/righthappy.ogg'),
    Sample('smartass', 'https://pajlada.se/files/clr/smartass.ogg'),
    Sample('ultralul', 'https://pajlada.se/files/clr/ultralul.ogg'),
    # Sample('yaranaika', 'https://pajlada.se/files/clr/yaranaika.ogg'),

    Sample('woah', 'https://pajlada.se/files/clr/woah.ogg'),
    Sample('realtrapshit', 'https://pajlada.se/files/clr/real-trap-shit.ogg'),

    Sample('actioniscoming', 'https://pajlada.se/files/clr/action-is-coming.ogg'),
    Sample('ting1', 'https://pajlada.se/files/clr/ting-1.ogg'),
    Sample('ting2', 'https://pajlada.se/files/clr/ting-2.ogg'),
    Sample('ting3', 'https://pajlada.se/files/clr/ting-3.ogg'),

    # Added 2018-05-28
    Sample('4head', 'https://pajlada.se/files/clr/2018-05-28/4head.ogg', '2018-05-28'),
    Sample('7777', 'https://pajlada.se/files/clr/2018-05-28/7777.ogg', '2018-05-28'),
    Sample('boyishgiggles', 'https://pajlada.se/files/clr/2018-05-28/boyishgiggles.ogg', '2018-05-28'),
    Sample('bruceuiscoming', 'https://pajlada.se/files/clr/2018-05-28/bruceuiscoming.ogg', '2018-05-28'),
    Sample('deadlycommandos', 'https://pajlada.se/files/clr/2018-05-28/deadlycommandos.ogg', '2018-05-28'),
    Sample('doot', 'https://pajlada.se/files/clr/2018-05-28/doot.ogg', '2018-05-28'),
    Sample('eatthepoopoo', 'https://pajlada.se/files/clr/2018-05-28/eatthepoopoo.ogg', '2018-05-28'),
    Sample('eshrug', 'https://pajlada.se/files/clr/2018-05-28/eshrug.ogg', '2018-05-28'),
    Sample('forsenswa', 'https://pajlada.se/files/clr/2018-05-28/forsenSWA.ogg', '2018-05-28'),
    Sample('howstrong', 'https://pajlada.se/files/clr/2018-05-28/howstrong.ogg', '2018-05-28'),
    Sample('hyperbruh', 'https://pajlada.se/files/clr/2018-05-28/hyperbruh.ogg', '2018-05-28'),
    Sample('levelup', 'https://pajlada.se/files/clr/2018-05-28/levelup.ogg', '2018-05-28'),
    Sample('nani', 'https://pajlada.se/files/clr/2018-05-28/nani.ogg', '2018-05-28'),
    Sample('pewdiepie', 'https://pajlada.se/files/clr/2018-05-28/pewdiepie.ogg', '2018-05-28'),
    # Sample('poi', 'https://pajlada.se/files/clr/2018-05-28/poi.ogg', '2018-05-28'),
    Sample('poopooiscoming', 'https://pajlada.se/files/clr/2018-05-28/poopooiscoming.ogg', '2018-05-28'),
    Sample('pphop', 'https://pajlada.se/files/clr/2018-05-28/pphop.ogg', '2018-05-28'),
    Sample('specimen', 'https://pajlada.se/files/clr/2018-05-28/specimen.ogg', '2018-05-28'),
    Sample('umad', 'https://pajlada.se/files/clr/2018-05-28/umad.ogg', '2018-05-28'),
    Sample('woop', 'https://pajlada.se/files/clr/2018-05-28/woop.ogg', '2018-05-28'),
]
