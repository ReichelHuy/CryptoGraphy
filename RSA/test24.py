# from sage.all import *
# def gcd(a, b):
#     while b:
#         a, b = b, a % b    
#     return a.monic()

# def FranklinReiter(c1, c2, e, n, a1, b1, a2, b2):
#     P.<X> = PolynomialRing(Zmod(n))
#     g1 = (a1*X + b1)^e - c1
#     g2 = (a2*X + b2)^e - c2
#     return int(-gcd(g1, g2).coefficients()[0])

# c1 = 2878541770875479700538980645022489052652779838963883862268026817166426417039919463236963390507307046326634703872280537467067742696639787192609769488919052545419119190066398990783581947278798037910506277397947588285998093950003094089963329770140593314668635940754481257775804384229002369671108815582459118647674550606119347487983453986281116009756152816183799880182210660978656475507140675089458058265971296259258268207468501053946378749643676641269894890364588680663491615255661967214865581346385880401292197870553292664912420303380215004099980768844056280656081194235775166437263428384802474463548807865519344521028
# c2 = 9358116384757608317220706970044933224234531757534430486726495081731537172532063758197094588560146034813412820720481673323181357275640282880376945873337874973608627166040471894089735428062869998336412925856834427099792181042190148866392208300871274345910645764652104826046243088695635872852698560499075328079478071928766314699067332677717903138094289636247404854454155325144516881573563576396070030232748258930392036341155059002641951617271533252090371171187191825436351873340387567232507741852632380312374845945384752378753935677949921080187872070947832676605655712908147214739222055430858304648290542768856843645161
# e = 11
# n = 16513150273488745819758318945465445929427923282220617948474026697826072849884410433840317590291164590606301920878166306100629001336979045875926362238578877426428184209782068217841561698268893281207281022882628671580544409079132228424570385789433865951296976542047938069538555185200454754405301473879058577591483273300132065945439952689462632448969760015421522358978863572507758617514279307992113676688788987384767873531588463072087737583220686506915075364580958023186096333340049114487946232564769897595127600679061991858554499358945100335619986316126901367151757694773827038242005563689706140134277497279550923802163
# a1 = 12971547059542234095294614655038910108921383446804620937171913894104315123703020491747060634311615668108873604447661547527993522223132139978046365817767051166630231776636365059125563542171499632449531108005444897410900841477831293648565180438324816667994353072194547726135161768865833107935141472738129346943372760468854044004065874712379448469666278516423795881542818175602189759347359757114386437400569740686015395353195882174948910859334443292433002434909568745424239403127792523066229466813140793214725997586482270739634637321902855765823212470124155976347852151938219301641131781157846722399123723376114259029831
# a2 = 11409457140242466819163427817479072385139033365230083718720047264434436898214384335636243055021460155275438092319802238955038605523688684385782916051156548581280516100417363773915481622407579450827246375873096305332208931991092735076355137904037100203515185779188885309077402419365710423222478825278182913737894421462042257973730289813359764845540728250586938424240047843075625738262558218714938963842910308398862881421355607305564841378461460037006115341626297306517807910746289965299025224005310222545925383605068291719567837393218166944929863737910844485524823699490307277435416628863671298960857171783974953402062
# b1 = 613773303374507022635125910125983319338750375401989130365990413259288154566000703324060713319607895380155378987796575897467664632420947636683945281102489734850754988807647012567280983450240026466967889841627553095079976456551370938474121254303474971902286679389596876001000910960884922282188621864881761290594293008441025880989824356804970700431082846079890191931506602887887043528887971319087988804158703119751734009927979973925960770863614397143971164317388792822866081412005500649012213609335946463233073780263602030911938670236561006470408586945289329597277998553381709448864453473541694078648267392748834582252
# b2 = 7245336764065642365831393452728740971259540086539413152250152735097680656770883053121301756868403120057747916744486252696211015549651622729853667084757925620818125696929068279230499982176189345006819380287349525312659226629850801073542291406883057493574547827172032691058542944679744377049745014959702974586433436512158229732186188003523586580642660072595199641524912132047912202451913864667343923032170547546966317318202888765453746148175214759547020579293565449701710859329968082044811127071473458891831112124821354298656439918625782443712556979595318257093732638944778996223990718369734263769019010362606613357004

# flag = FranklinReiter(c1, c2, e, n, a1, b1, a2, b2)
# print(bytes.fromhex(hex(flag)[2:]).decode())
