#aqui irá el dia uno que a su vez es la continuación del cap1

default rutabuena = None
default rutaneutra = None

label cap2:

    $ ach_chapter2 = True
    $ ach_good_ending = True
    $ ach_secret_scene = True
    $ ach_all_yuri_poems = True

    play music audio.t6 fadein 2.0
    scene bg corridor

    with dissolve_scene_full

    "Seguí a Sayori por los pasillos, Comunmente subimos aqui por materiales."

    "Sé que es un club con poca gente pero el que este tan alejado no ayuda"

    play audio closet_open

    "Sayori abrió la puerta del salón con fuerza."

    mc "¿No era más fácil abrirla gentilmente?"

    scene bg club_day

    show sayori 1s zorder 2 at f11

    s "¡¡¡Chicas!!! ¡¡¡traje a un nuevo miembro!!!"

    show sayori 1q zorder 2 at t11

    mc "No lo grites sayori..."

    "¿Chicas?"


    show sayori 1q zorder 2 at thide
    hide sayori

    with wipeleft_scene 
    #sirve para hacer una transición de izquierda a derecha, también se puede usar wiperight_scene, wipeup_scene, wipedown_scene

    "Mi mirada se centró en una estudiante de pelo morado."

    show yuri 2b zorder 2 at f11

    y "Bienvenido al club de literatura, es un placer conocerte [player]."

    show yuri turned rup uniform happ om ce zorder 2 at f11

    y "Sayori siempre nos habla bien de ti."

    y "Me alegra mucho poder conocerte."   

    show yuri turned lup rup uniform nerv cm oe zorder 2 at t11

    y "(¿Espera por qué dije eso en voz alta?)"

    show yuri turned lup rup uniform nerv cm oe zorder 2 at f11

    y "Uh..." 

    show yuri turned lup rup uniform nerv cm oe zorder 2 at t11

    pause 1.0

    show yuri turned rup uniform lsur cm oe zorder 2 at t11

    "Dios... es como si viera un angel en persona."

    "Es tan linda."

    "Aunque recuerdo como si la hubiera visto fuera de la escuela..."

    "Su cabello es hermoso..."

    n "¿Enserio era necesario un chico?"

    show yuri shy neut cm oe zorder 2 at t22


    show natsuki 1h zorder 2 at f21

    n "Qué incómodo será el club desde ahora."

    show yuri shy neut cm oe zorder 2 at t32

    show natsuki 2g zorder 2 at t31

    show monika 4b zorder 2 at f33

    m "¡Ey! que bonita sorpresa [player]"

    show natsuki 2g zorder 2 at t31

    show monika 2k zorder 2 at f33

    m "bienvenido al club de literatura"

    show monika 2j zorder 2 at t33

    "Sayori... Sayori me trajo a un club..."

    show monika zorder 2 at thide
    hide monika

    show natsuki zorder 2 at thide
    hide natsuki

    show yuri 1d zorder 2 at t11

    "¡Qué tiene a una chica tan linda!"

    show yuri 1e zorder 2 at t21

    show natsuki 2w zorder 2 at f22

    n "¿Qué nunca has visto a una mujer?"

    show yuri 1e zorder 2 at t21

    show natsuki turned anno cm oe zorder 2 at t22

    mc "Dis-disculpa."

    show yuri 1w zorder 2 at t42

    show natsuki 2w zorder 2 at t44

    y "Natsuki... recuerda que es nuestro nuevo miembro."

    show yuri 1w zorder 2 at thide

    hide yuri

    show natsuki 3i zorder 2 at t11

    "Parece que la chica de cabello rosado es un poco dificil..."

    "Por su apariencia será alguien de primer año asi que no vale la pena enojarse con ella."

    "¿Le dijo Natsuki? probablemente sea quien hizo los pastelitos."

    show yuri 2i zorder 2 at t32

    show natsuki 3i zorder 2 at t33

    show sayori turned happ om ce zorder 2 at f31

    s "Tranqui [player], solo ignorala cuando esté de mal humor."

    show sayori turned happ cm ce zorder 2 at t31

    "Sayori se acercó a mi sonando sus pasos contra el suelo."
    show yuri 2i zorder 2 at thide
    show sayori turned happ om ce zorder 2 at thide 

    hide yuri

    hide Sayori

    show natsuki 3f zorder 2 at f11

    s "¡De todos modos! ella es Natsuki."
    show natsuki 3f zorder 2 at thide 

    hide natsuki 

    show yuri 3a zorder 2 at t11

    s "Yuri."

    hide yuri 

    show monika lean happ om ce zorder 2 at t11

    s "Monika."

    hide monika

    show sayori 1s zorder 2 at f11

    s "¡Y tu ya me conoces!"

    show sayori zorder 2 at thide
    hide sayori 

    show yuri shy happ cm oe zorder 2 at t11

    "Aunque Sayori me este presentando a las demás chicas no puedo quitar la mirada de Yuri..."

    "Monika se acercó a mi con una amable sonrisa."

    show yuri zorder 2 at thide
    hide yuri 

    show sayori turned lsur cm oe zorder 2 at t21 

    show monika forward lpoint happ om oe zorder 2 at f22

    m "De hecho [player] y yo estuvimos en la misma clase el año pasado"

    show monika forward happ cm ce zorder 2 at t22

    "Ella es Monika recuerdo perfectamente que estuvimos en la clase de Quimica el año pasado..."
    
    "Prefiero olvidar lo que pensaba el año pasado."

    show monika forward happ om oe zorder 2 at f22

    m "Que alegria es verte de nuevo [player]"

    show monika forward happ cm oe zorder 2 at t22

    mc "Si... es un gusto también"

    show sayori turned happ om oe zorder 2 at f21

    s "¡Ven [player]! ya tengo mucha hambre."

    show sayori zorder 2 at thide
    hide sayori 

    show monika zorder 2 at thide
    hide monika 



    "Las chicas formaron un circulo con los pupitres mientras que Sayori me sentó a su lado."

    "Al ver a las demas chicas excepto a Yuri supe de quien era el asiento faltante a mi lado."

    show sayori tap nerv m1 zorder 2 at f21

    s "Ya regreso~"
    hide sayori
    with wipeleft_scene

    show sayori 4p zorder 2 at f11

    s "Realmente no me podia aguantar las ganas de comer los pastelitos, Natsuki es la mejor cocinera... ¿o pastelera?"

    show sayori 4q zorder 2 at t22

    show natsuki 3f zorder 2 at f21

    n "¡Sayori!"

    show natsuki 3f zorder 2 at t21

    stop music fadeout 2.0

    "La pelirosa agarró bruscamente la bandeja pero debido al movimiento ella terminó cayendo al suelo."

    play sound obj_fall
    show natsuki 3f zorder 2 at h21

    n "off...-{nw}"

    show natsuki zorder 2 at thide
    hide natsuki 

    show sayori 4m zorder 2 at t21

    show monika 1g zorder 2 at t22

    play music audio.t9

    mc "¿Te encuentras  bien?"

    "Me levanté de mi asiento, mientra Sayori ayudaba a Natsuki a levantarse. Recogí la bandeja"

    show sayori zorder 2 at thide
    hide sayori

    show monika zorder 2 at thide
    hide monika

    show natsuki 2b zorder 2 at f11

    n "U-uh... mi cabeza... ¿¡y los pastelitos!? [player] deja lo-"

    show natsuki turned curi cm oe zorder 2 at t11

    "Aunque un par de pastelitos estaban caidos en el suelo logré rescatar algunos."

    show natsuki turned lsur cm oe zorder 2 at t11

    "Todos estan decorados como si fueran gatitos, realmente se mira el talento."

    show natsuki turned fs neut om oe zorder 2 at f11

    n "L-lo siento... Quería mostrarlo por mi misma realmente me esforcé mucho haciendolo..."

    show natsuki turned fs neut cm oe zorder 2 at t11

    "Natsuki está muy centrada en los pastelitos del suelo."
    
    show sayori 1f zorder 2 at t21

    show natsuki turned fs neut cm oe zorder 2 at t22

    "Sayori también."

    "Como puedo ayudar... con la bandeja en mi mano me di cuenta que aun quedaban unos pastelitos"

    mc "Oigan esta bien... miren no todos cayeron al piso..."

    show sayori 1l zorder 2 at t21

    show natsuki 1n zorder 2 at t22

    mc "Y... se miran muy delicisosos ¿no?"

    show sayori 3b zorder 2 at t21

    show natsuki turned lhip rhip ff sad om oe zorder 2 at f22

    n "S-si..."

    show natsuki 4b zorder 2 at t22

    show natsuki turned lhip rhip ff sad cm oe zorder 2 at t22

    show sayori turned happ om oe zorder 2 at f21

    s "¡Siii! aún hay pastelitos"

    show natsuki turned lhip rhip ff pout cm oe zorder 2 at f22

    n "Ajah..."

    show natsuki zorder 2 at thide
    hide natsuki

    show monika 2m zorder 2 at t21

    show sayori 1q zorder 2 at t22

    "Natsuki se fue al closet a buscar algo para limpiar el piso"

    "Mientras que Sayori se acerco a mi oido"

    show monika zorder 2 at thide
    hide monika

    show sayori 1c zorder 2 at f11

    s "[player]"

    show sayori 1a zorder 2 at t11

    mc "¿Eh?"

    show sayori 1c zorder 2 at f11

    s "Hiciste bien"

    show sayori 1a zorder 2 at t11

    mc "Tenia que hacer algo para animarlas ¿no?"

    show sayori 3c zorder 2 at f11

    s "Como siempre jeje.."

    show sayori 3b zorder 2 at t11

    mc "¿Siempre?"

    stop music fadeout 2.0

    play music audio.t8 

    show sayori 2r zorder 2 at f11

    s "¡Vamos a comer~!"

    show sayori 1a zorder 2 at t22

    show monika forward lpoint happ cm ce zorder 2 at t21

    "Despues de hablar agarró rápidamente un pastelito de la bandeja, seguida de Monika y luego de mi"
    show sayori turned happ om ce zorder 2 at h22
    s "Esh mu delichisosho~ hmm~"
    show monika forward lpoint happ cm oe zorder 2 at t21

    "Mientras Sayori comia Natsuki salió del closet con un trapo y empezó a limpiar el piso"

    "Despues de que Natsuki terminará de limpiar el piso se sentó al lado de Sayori"

    show sayori zorder 2 at thide
    hide sayori

    show monika zorder 2 at thide
    hide monika

    show  natsuki 3n zorder 2 at t11

    "Noto como mira en mi dirección mientras comía el pastelito"

    mc "Sayori tenia razón estan muy deliciosos"

    show natsuki 3r zorder 2 at t11

    mc "Muchas gracias, Natsuki"

    show natsuki 3r zorder 2 at f11

    n "¡N-no es que los haya hecho para ti o algo asi!"

    "Sayori dijo que eran para el nue- sabes... mejor sigo disfrutando de los dulces pastelillos"

    show natsuki zorder 2 at thide
    hide natsuki

    with wiperight_scene

    show yuri 2a zorder 2 at t33

    "Yuri regresó con un juego de té en la mano y me entregó una taza con té"

    mc "¿los profesores no las regañan por tener esto?"

    show yuri 2b zorder 2 at f33

    y "nos dieron permiso debido a ser un nuevo club"

    y "además, una taza de té siempre va de la mano de un libro"

    show yuri 2o zorder 2 at t21

    show monika 3b zorder 2 at f22

    m "tranquilo [player], solo intentan impresionarte"

    show monika 1h  zorder 2 at t22

    m "(¿presumiendo?)"

    show yuri 2o zorder 2 at f21

    show monika 2j zorder 2 at t22

    y "¿qu-que...? y-yo no intentaba..."

    show yuri 2o zorder 2 at t21

    "Yuri volteó su mirada hacia la nada"

    show yuri 2w zorder 2 at f21
    show monika forward lpoint rhip happ cm oe zorder 2 at t22

    y "t-tu me entiendes..."

    show yuri zorder 2 at thide
    hide yuri

    show monika lean happ om oe zorder 2 at f11

    m "por cierto [player], me alegra que te hayas unido, como presidenta del club me aseguraré que te sientas cómodo"

    show monika lean happ om oe zorder 2 at t11

    stop music fadeout 2.0

    mc "¿que me haya unido? pero aun no me he decidido en unirme..."

    show monika zorder 1 at thide
    hide monika

    show sayori 2m zorder 2 at t11

    mc "me refiero..."

    show sayori 2m zorder 2 at t21

    show yuri 2i zorder 2 at t22

    mc "aún tengo que ver otros clubs..."

    show sayori 2m zorder 2 at t31

    show yuri 2i zorder 2 at t32

    show monika 1m zorder 2 at t33

    mc "ver que club me gusta mas..."

    show sayori 2m zorder 2 at t41

    show yuri turned sad cm oe zorder 2 at t42

    show monika 1m zorder 2 at t43

    show natsuki 1h zorder 2 at t44

    "Vamos no pueden mirarme todas asi"

    "Después de conocer a Yuri tal vez las cosas no sean tan malas, además no quiero que Sayori siga acosandome con que entre a su club"

    "Tome valor y mire a las chicas directamente"
    mc "eh... tomé una desición"

    "todas las chicas me estaban viendo esperando mi respuesta"

    show sayori 2q zorder 2 at t41

    show yuri 1a zorder 2 at t42

    show monika 1j zorder 2 at t43

    show natsuki 2f zorder 2 at t44
    play music audio.t8
    mc "esta bien... si me uniré al club"

    show sayori 2r zorder 2 at h41

    s "¡yeiiii! por un momento pensé que no te unirías"

    "Sayori me agarró de las manos y empezo a saltar con mucha emoción"

    show natsuki 1e zorder 2 at f44

    n "si hubieras dicho que no te unirías te hubiera hecho pagar por el pastelito"

    show natsuki 1g zorder 2 at t44

    show yuri 1d zorder 2 at f42

    y "me asustaste por un instante"

    show yuri 1d zorder 2 at t42

    show monika 1b zorder 2 at f43
    
    m "me alegra que hayas tomado una buena desición"

    show natsuki zorder 2 at thide
    hide natsuki

    show sayori zorder 2 at thide
    hide sayori

    show yuri zorder 2 at thide
    hide yuri

    show monika 2b zorder 2 at f11

    m "Tengo una idea. Ya que [player] se ha unido, podriamos organizar una actividad, ayer me encontré con algo curioso..."

    show monika zorder 2 at thide
    hide monika

    show sayori 2n zorder 2 at f11

    s "¿actvidad?"

    show sayori zorder 2 at thide
    hide sayori

    show monika 3a zorder 2 at t11

    "monika sacó una hoja"

    show monika 3b zorder 2 at f11

    m "no sabía que te gustaba escribir poemas, Natsuki" 

    show monika 3a zorder 2 at t21

    show natsuki turned lhip rhip vang cm ce zorder 2 at f22

    n "¡dame eso Monika!"

    "natsuki agarro la hoja de las manos de Monika para luego meterla en su mochila"

    show natsuki zorder 2 at thide
    hide natsuki

    show monika forward lpoint happ om ce zorder 2 at f11

    m "y bueno... estaba pensando en que podriamos compartir poemas asi para [player] será mas fácil conocernos"

    show monika 2i zorder 2 at f11

    m "pero no creas que te salvarás de escribir uno también [player]"

    show monika 2m zorder 2 at f11

    mc "uh... claro"

    show sayori turned lup rup happ om ce zorder 2 at f21

    show monika 2i zorder 2 at t22

    s "cuando llegue a casa me pondre a escribir"

    show sayori 1a zorder 2 at t31

    show monika 2i zorder 2 at t32

    show natsuki cross vang om ce zorder 2 at f33

    n "que verguenza... no me gustaria compartir mis poemas, estoy segura que el nuevo me entenderá"

    show sayori 1a zorder 2 at t41

    show monika 2i zorder 2 at t42

    show natsuki cross anno cm oe zorder 2 at t43

    show yuri shy neut om oe zorder 2 at f44

    y "para mi... tambien seria dificil hacerlo"
    show yuri shy neut om oe zorder 2 at f44

    show monika forward rhip happ cm oe zorder 2 at t42

    "monika se quedó en silencio por un momento, para luego mirarme con una sonrisa"

    mc "supongo que... podria hacer un poema y decirlo y eso"

    show monika forward rhip happ om oe zorder 2 at f42

    m "perfecto yo también, asi que chicas y [player] doy por concluida la reunion del club por hoy"

    show natsuki zorder 2 at thide
    hide natsuki

    show monika zorder 2 at thide
    hide monika

    show yuri zorder 2 at thide
    hide yuri

    show sayori zorder 2 at thide
    hide sayori

    show yuri turned laug cm oe zorder 2 at t11

    "siento mucha ansiedad por escribir un poema {i}y encima compartilo con ellas, ella{/i}"

    "yuri se levantó de su asiento para ayudar a limpiar a Natsuki"

    show yuri zorder 2 at thide
    hide yuri

    show sayori turned happ om oe zorder 2 at f11

    s "oye [player] ya que desde ahora nos veremos todos los dias, ¿quieres caminar conmigo a casa? ya sabes como lo haciamos antes"

    "es cierto, hace mucho tiempo que no caminaba con Sayori debido a lo tarde que salia, no solo de la escuela"

    menu irse_con_Sayori:
        "Irse con Sayori":
            "Si, deberia ir con ella"
            $ rutabuena = "Se eligió ir con Sayori"
        "Mejor no":
            mc "mejor no"
            $ rutaneutra = "Se rechazó ir con Sayori"
    call rutas        


    label biblioteca:

        show bg bedroom
        with dissolve_scene_full
        play music audio.t8

        "agarré un lapiz y una hoja de papel"

        "
        poemas, poemas"

        "¿cómo siquiera se escribe un poema?"

        "Yuri luce como una chica madura por lo que imagino que le gustaran los poemas reflexivos o algo así"

        "golpeo repetidamente el lapiz contra el escritorio intendo hallar inspiración"

        "uff... si tan solo pudiera escribir palabras random que suenen bien..."

        "¡SI!"
  
        "la biblioteca a estas horas está abierta y puedo inspirarme, solo debo de buscar algo que le guste a Yuri..."
        "Si me apresuro llegare antes de que cierren la biblioteca"
        stop music fadeout 1.5
        show black 
        with dissolve_scene_full
        "Un poco agotado y con algunas gotas de sudor tomo aire antes de entrar a la biblioteca"
        scene bg library_aft
        with dissolve_scene
        play music audio.heartbreaking2 fadein 2.0

        "Uff aun sigue abierta"
        "El silencio de la biblioteca siempre me tranquiliza"
        "A lo lejos veo un par de estudiantes leyendo unos cuantos libros y a la bibliotecaria hablando con un señor mayor"
        "Parece querer llevarse un libro sobre cocina"
        "Como sea..."
        "Saliendo de mi trance empiezo mi busqueda de libros que podrian interesarle a Yuri"

        "agarro varios libros que parecen de terror y reflexivos"

        "espero no estarme guiando por una apariencia..."

        "La llamada de Cthulhu...{w} muy complicado"

        "¿Books of Blood?{w} suena como si fuera escrito por un adolescente edgy"

        "El hombre de arena.{w} ¿Ese no era un enemigo de un superhéroe?"

        "¿exit music: redux?{w} me suena de algo..."

        show silueta zorder 2 at f11

        "Chico Friki" "Con permiso"

        show silueta zorder 2 at t11

        "el tipo me arrebató el libro de la mano"

        show silueta zorder 2 at f11

        "Chico Friki" "por favor dime que no lo vas a comprar... hace tiempo que lo he estado buscando es muy bueno"

        show silueta zorder 2 at t11

        mc "eh... si está bien ¿lo entiendo?"

        show silueta zorder 2 at thide
        hide silueta

        "caminé al siguiente pasillo, iba a agarrar otro libro pero senti como alguien me dio un pequeño empujón"

        "me volteé rapidamente"

        show monika 1 zorder 2 at t11

        mc "ah... eres tu"

        show monika forward neut n2 mg e1a b2b zorder 2 at f11

        m "perdona no queria asustarte"

        show monika forward neut n1 ma e1a b2b zorder 2 at t11

        "por un momento sentí que me habia congelado"

        mc "no te procupes... y ¿que haces por aqui?"

        show monika forward lpoint happ om oe zorder 2 at f11
    
        m "busco algunas partituras de piano, ultimamente he intentado aprender a tocar el piano"

        show monika forward lpoint happ cm oe zorder 2 at t11

        mc "oh, eso suena genial"

        show monika forward lpoint happ om ce zorder 2 at f11
    
        m "ya que respondí, es mi turno preguntar ¿que hace [player] aqui?"

        show monika forward lpoint happ cm ce zorder 2 at t11

        "¿que estaba haciendo?{w}, ahh si"
    

        mc "estaba buscando algo, ya sabes como me uni al club queria estar más al tanto"

        show monika forward lpoint happ om oe zorder 2 at f11


        m "ya veo. ¿Te gusta el terror, no?"

        show monika forward lpoint happ cm oe zorder 2 at f11

        mc "algo asi..."

        show monika lean m3 e4 b1 zorder 2 at f11
    
        m "dejame adivinar, quieres impresionar a alguien inspirandote en un libro, ¿cierto?"

        show monika lean m1 e4 b1 zorder 2 at t11

        mc "eh..."

        show monika lean m3 e1 b1 zorder 2 at f11
    
        m "jeh, no fue tan dificil leerte"

        m "entonces pien-..."

        show monika lean m1 e1 b1 zorder 2 at thide
        hide monika

        show yuri shy neut cm oe zorder 2 at t33

        "monika me estuvo hablando, sin embargo vi a alguien a los lejos, una chica de pelo morado"

        show yuri shy neut cm oe zorder 2 at thide
        hide yuri

        show monika forward curi om oe zorder 2 at f11
    
        m"[player]"

        mc "Esa chica... ¿es Yuri?"
        show monika forward curi om oe zorder 2 at thide
        hide monika 
        show yuri turned anno om oe zorder 2 at t11

        "monika se volteó y efectivamente era Yuri con un par de libros"

        mc "y ahora entrará Sayori"

        "mencione con una sonrisa intentando hacer un chiste"
    
        "monika no reaccionó ante lo que dije"
        show yuri turned anno om oe zorder 2 at t11
        hide yuri 
        show monika forward anno cm oe zorder 2 at t11
        mc "¿monika?"

        "monika inmediatamente volvió a la realidad"
        stop music fadeout 2.0

        show monika forward dist om oe zorder 2 at f11
        m "[player]... ¿hay un problema si te hago una pregunta?"
        show monika forward dist cm oe zorder 2 at t11

        mc "no tendria problema, adelante"
    
        show monika forward dist om oe zorder 2 at f11
        m "¿qué opinas de las chicas del club?"
        show monika forward dist cm oe zorder 2 at t11

        "¿qué tipo de pregunta es esa?"

        "por alguna razón Monika me lo pregunta seriamente"

        mc "bueno... ehh las chicas... "

        mc "Sayori... si, Sayori y yo nos conocemos desde pequeños, somos amigos de la infancia y se podria decir que es mi mejor amiga"

        mc "tu pues me agradas, ya te conocía hace un tiemp-{nw}"

        show monika forward pout om oe zorder 2 at f11
    
        m "¿y yuri?"

        show monika forward pout cm oe zorder 2 at t11

        mc "¿yuri?"

        show monika forward nerv om oe zorder 2 at f11
        m "bueno noté que la mirabas mucho"
        show monika forward nerv cm oe zorder 2 at t11
    
        mc "no creo que haya pasado eso"
        show monika forward rhip pout om oe zorder 2 at f11

        m "pero pasó..."
        m "yuri es un poco timida con los demás sobre todo con nuevas personas"

        show monika forward lpoint neut om oe zorder 2 at f11
    
        m "y seria una pena si se fuera porque alguien la hace sentir incomoda en el club..."

        show monika forward lpoint neut cm oe zorder 2 at t11

        mc "monika entiendo eso pero yo nunca incomodaría a alguien y mucho menos a Yuri"

        m "..."

        show monika forward lpoint pout om oe zorder 2 at f11
        m  "está bien... pero mantente alejado de ella. Creeme ella siempre está mejor sola"
        show monika forward pout cm oe zorder 2 at t11

        mc "..."


    
        "realmente no se que decir, como podria alejarme o evitar a Yuri"
        "No puedo hacer eso"

        play music audio.heartbreaking2 fadein 2.0

        show monika forward neut om oe zorder 2 at f11
        m "bueno me tengo que retirar, hasta mañana [player] cuidate"
        show monika forward neut cm oe zorder 2 at t11
        mc "Hasta pronto Monika"
        show monika forward neut om oe zorder 2 at thide 
        hide monika

        "Veo como monika camina hacia la salida"
        "No logro ver a Yuri en el mismo lugar que la vi antes"

        "Supongo que Yuri se ha ido"

        "no creo que realmente esté incomodando a Yuri... o que podria hacerlo"

        "quizás este sobrepensado, es la presidenta del club obviamente querrá lo mejor para... para el club"
        "N-no deberia darle tantas vueltas ahora"
        "Revise las estanterias y lleve conmigo unos cuantos libros para continuar con la tarea que me espera en casa"

        "El mismo silencio que me recibio antes me despide mientras camino fuera de la biblioteca de camino a casa"
        scene bg bedroom
        with dissolve_scene_full
        "Saco los libros de mi mochila y los apilo cerca de mi escritorio"
        "ver la pila de libros me hace sentir abatido"
        "Con papel y lapiz en mano, suspiro"
        mc "Me espera una laaarga noche"
        stop music fadeout 2.0
        show black
        with dissolve_scene_full

    
    #al siguiente dia
    #día 2
    label dia2:
    scene bg club_day
    with dissolve_scene

    play music audio.t6 
    show monika lean happ om oe zorder 2 at f11 
    m "hola [player]"
    m "me alegra saber que no escapaste"
    show monika lean happ cm oe zorder 2 at t11

    mc "soy alguien de promesa, que puedo decir."
    show monika lean zorder 2 at thide
    hide monika 

    "¿llegué tarde?, parece que las demas chicas ya llevaban un rato en el club"
    show yuri turned lup rup happ om ce zorder 2 at f11
    
    y "sabia que cumplirias con tu promesa [player]"
    y "espero no te agobie el leer libros, sé como se siente cuando no estas acostumbrado"
    show yuri turned lup rup doub cm ce zorder 2 at t21
    show natsuki cross neut om oe zorder 2 at f22
    n "no le tengas piedad, Sayori me dijo que aceptaste venir cuando mencionó los pastelitos"

    show natsuki cross doub om oe zorder 2 at f22
    n "asi que tómate enserio esto, si tienes hambre en el segundo piso está el club de cocina"
    show natsuki cross doub cm oe zorder 2 at t22

    show yuri turned flus cm oe zorder 2 at f21
    y "disculpa Natsuki, estaba hablando con [player]..."
    show yuri turned flus cm oe zorder 2 at t21

    show natsuki cross angr om ce zorder 2 at f22 
    n "oye solo quiero que nos tome en serio, no permitire que arruine nuestro club"
    show yuri turned happ cm oe zorder 2 at t31
    show natsuki cross angr om ce zorder 2 at t32
    show monika lean happ om oe zorder 2 at f33 
    m "¿no es un poco dificil hablar asi para alguien que tiene una coleccion completa de manga en el salón?"
    show monika lean happ om oe zorder 2 at t33 

    show natsuki n3 turned shoc om oe zorder 2 at f11
    n "¡¡MON-MAN-MON-MAN!!"
    show natsuki n3 turned shoc om oe zorder 2 at t11

    "natsuki se quedo atascada en decir Monika o manga"
    show natsuki turned shoc om ce zorder 2 at f32
    n "el manga es literatura"
    show natsuki turned shoc om ce zorder 2 at thide
    hide natsuki

    "natsuki se giró y entro dentro del closet del salón"
    show monika forward happ cm oe zorder 2 at thide
    hide monika
    show sayori turned happ om oe zorder 3 at t21
    show yuri turned flus cm oe zorder 2 at t22
    

    show sayori turned happ om ce zorder 2 at f21
    s "tranquilas chicas, [player] siempre apoya cuando algo le interesa... o le piden ayudas jeje..."
    show sayori turned happ om oe zorder 2 at t21

    "Como ordenar tu cuarto"

    show yuri lup rup happ om ce zorder 2 at f22
    y  "que considerado"
    show yuri lup rup happ cm ce zorder 2 at t22

    mc "como me gustaria decir que no es dificil... como salvar una casa apunto de incendiarse"
    show sayori ml e4c b1c zorder 2 at f21
    s "¡eso jamás pasó!"
    show sayori mk e4c b1c zorder 2 at t21

    mc "¿entonces lo estoy inventando?"

    show sayori tap pout om oe  zorder 2 at f21
    s "ush si que eres malvado..."
    show sayori tap pout cm oe  zorder 2 at t21

    show yuri turned ldown happ om oe zorder 2 at f22
    y "¿son muy buenos amigos no?"

    y "quizas este un poco celosa"

    show sayori turned happ om oe zorder 2 at f21
    s "¿celosa? ¡pero tu y [player] tambien pueden ser buenos amigos!"
    show sayori turned happ cm oe zorder 2 at t21

    show yuri turned flus cm oe zorder 2 at f22
    y  "u-uhm..."
    show yuri turned flus cm oe zorder 2 at t22

    mc "sayori..."

    show sayori turned happ om oe zorder 2 at f21

    s "¿si?"

    s "ahh por cierto Yuri te trajo un regalo"
    show sayori turned happ cm oe zorder 2 at t21

    show yuri turned lup pani om oe zorder 2 at f22
    y "n-no es importante"

    show yuri shy neut om oe zorder 2 at f22
    y "pe-pero si prefieres no aceptar mi regalo esta bien..."
    show yuri shy neut cm oe zorder 2 at t22

    "¿un regalo? ni siquiera en un sueño me imaginaria esto"
    
    mc "oye es una gran sorpresa, no pensaba que iba a recibir algo"

    mc "y cualquier cosa, es bienvenida"

    show yuri shy happ om oe zorder 2 at t22
    y "..."
    show yuri shy happ om oe zorder 2 at thide
    hide yuri

    "Yuri caminó hacia su asiento buscando algo en su silla"

    show sayori turned happ om ce zorder 2 at f21
    s "[player] estoy segura que te gustará jeje..."
    show sayori turned happ cm oe zorder 2 at t21

    "¿seguimos hablando del regalo?"
    show sayori turned happ om ce zorder 2 at thide
    hide sayori

    "Yuri regresó con un libro en la mano"
    show yuri shy happ cm oe zorder 2 at f11

    y "queria regalarte un libro... pensé que te gustaría ya que eres nuevo"

    show yuri shy neut om oe zorder 2 at f11
    
    y "y en cualquier momento"

    y "o cuando termines"
    
    y "podriamos..."

    show yuri shy neut n5 zorder 2 at f11
    y "compartir opiniones"
    show yuri shy neut cm oe zorder 2 at t11

    mc "¡muchas gracias Yuri! realmente no se mucho de literatura pero lo leeré"
    show yuri turned lsur om ce zorder 2 at t11
    "agarré el libro y yuri se relajó"

    show yuri turned happ om ce zorder 2 at f11
    s "estoy emocionada de saber que opinas"
    show yuri turned happ cm oe zorder 2 at t11
    mc "No puedo esperar a empezar a leerlo"
    mc "De nuevo muchas gracias Yuri"
    show yuri turned happ om ce zorder 2 at thide
    hide yuri
    scene bg club_day
    with wipeleft_scene
    
    "llevo un tiempo sentando sin hablarle a nadie"

    "aunque quiero hablarle a Yuri no quiero incomodarla... está muy centrada en su libro"

    "¿qué estará leyendo?"

    "me centré en su libro, es muy parecido al que me regalo"
    show yuri turned pani om oe zorder 2 at h11
    y "uh-ah..."
    show yuri turned flus cm oe zorder 2 at s11
    "yuri noto mi mirada, cuando me miro a los ojos inmediatamente escondio su rostro bajo el libro"

    "Tal vez deberia pedirle disculpas"

    mc "perdona, solo estaba interesado en el libro"

    mc "Sobre que trata, si no te molesta que te pregunte"

    show yuri turned flus om oe zorder 2 at f11
    y "N-no te preocupes"
    show yuri turned flus om oe zorder 2 at s11
    y "fuh... el libro, basicamente trata sobre una mujer y su marido encerrados en un campamento"

    show yuri turned lsur om ce zorder 2 at f11
    y "son torturados y custodiados por lo que hacen un plan para escapar, al tratar de escapar son descubiertos y como castigo"

    y "ordenaron al marido ver como su esposa era colgada por 10 minutos mientras su cadaver inerte se palidecia cada vez más"

    y "el marido fue confinado en un lugar donde la luz del sol era nula"

    y "Poco a poco el hombre sucumbia ante la locura"

    y "Mantenia alucinaciones sobre la muerte de su esposa, su desesperacion por la falta de aire, el dolor de la soga en su cuello"

    y "el hombre se ahorcaba con sus propias manos tratando de buscar la misma sensación que sintio su esposa"

    y "La soledad acompañada de una eterna oscuridad eran el martirio de aquel hombre que luchaba por mantener su cordura"

    show yuri turned lsur cm ce zorder 2 at t11


    "aunque la voz de Yuri ayuda a que no suene tan mal... es una historia muy oscura"


    "yuri al ver mi rostro parece haber vuelto a la realidad"

    show yuri turned nerv om oe zorder 2 at f11

    y "L-lo siento empece a divagar, seguro piensas que soy rara por leer este tipo de libro"

    y "ni siquiera estas acostumbrado a leer muchos libros y...{nw}"

    mc "No tienes de que preocuparte Yuri, no tienes que esconder la pasión que tienes por la lectura"

    mc "Despues de todo estamos en el club de literatura, ademas no me molesta en absoluto escucharte hablar"

    mc "Por favor continua"

    y turned sad om oe "Uh-Ah, suelo leer historias un tanto diferentes. Me gustan porque puedes ver la vida desde otro punto de vista"

    y "no siempre todo final malo es... malo{w}, algunos te hacen reflexionar y aprendes tantas cosas de los personajes sin tener que decirlas directamente"

    show yuri turned nerv om oe zorder 2 at h11

    y "¡perdón! aveces hablo demas de los temas que me interesan"

    mc "no, esta bien si hablas mucho de algo es porque te interesa, ¿cierto?"

    mc "ademas... suena interesante, podriamos leerlo"

    y turned laug om oe "bu-bueno"

    mc "tu libro se parece al que me regalaste ¿son del mismo autor?"

    y "en realidad es el mismo libro"

    mc "oh, entonces eso hace mas facil que podamos leerlo"

    show yuri turned laug om oe zorder 2 at thide
    hide yuri

    "saqué el libro de mi mochila y comencé a leerlo a la par de Yuri"

    show yuri shy m1 e3 b1 zorder 2 at t11

    "Mientras leia el libro podia ver de reojo como Yuri estaba viendome"
    show yuri shy m4 e3 b1 zorder 2 at h11
    y "lo-lo siento"

    mc "¿Yuri no crees que te disculpas demasiado?, no has hecho nada malo"

    show yuri turned rup flus cm oe zorder 2 at h11

    y "¿lo hago?, perdon... N-NO ¡quiero decir!-"

    mc "quizas asi ambos podemos leer mejor"

    "deslice mi pupitre hasta juntarlo con el de Yuri y agarré mi libro para sostenerlo de un lado"

    "yuri se inclinó un poco para sostener el libro con su mano izquierda"

    show yuri turned rup flus cm oe zorder 2 at thide
    hide yuri
    pause 0.8
    scene y_cg1_base
    show y_cg1_exp1

    mc "aunque no habia pensado en como cambiaremos de pagina"

    mc "¿lees rapido?"

    y "uh... suelo leer con calma..."
    hide y_cg1_exp1 with dissolve 

    "me quedé en silencio cuando sentí el hombro de Yuri. estamos mas cercanos que antes"

    "intenté concentrarme en leer"

    #probablemente poner libro

    with dissolve_scene_full

    show y_cg1_exp1 with dissolve 

    y "¿listo?"
    

    "yuri dejo de leer el libro para mirarme"

    mc "ah... en realidad no he terminado aún"

    y "¿no sueles leer mucho cierto?"
    show y_cg1_exp2 with dissolve 
    y "puedo ser paciente contigo, mostraste interés en la historia asi que es lo minimo que puedo hacer"

    mc "s-si"

    mc "muchas gracias Yuri"
    hide y_cg1_exp2 with dissolve 
    hide y_cg1_exp1 with dissolve 

    "Creo que Yuri ya había terminado antes de que yo acabara la primera página"

    with wipeleft_scene

    "terminé el capitulo, intuyo que Yuri también asi que intento pasar de página"

    "cuando intento mover la hoja Yuri me ayuda con su mano izquierda"

    mc "¿sabes? el personaje principal me recuerda a ti"
    show y_cg1_exp1 with dissolve
    y "¿enserio?"

    mc "buneo... por lo menos en algunos gestos que sueles hacer"
    show y_cg1_exp3 with dissolve
    y "y-ya v-veo"
    hide y_cg1_exp3 with dissolve
    hide y_cg1_exp1 with dissolve 
    "Yuri se mantuvo en silencio parece pensar en algo"
    scene bg club_day 
    with dissolve
    show yuri shy happ om oe zorder 2 at h11
    y "que digas eso... ¡es muy malo que me parezca a el!"

    "Yuri jugó con uno de sus mechones. creo que le dije algo que la avergonzó"

    mc "¡n-no intentaba decir algo malo!"

    "perfecto arruine todo en una linea"

    mc "no intentaba decirlo de manera negativa sino... como algo... algo lindo"

    y shy n3 m3 e1 b1 "¿Lin-lindo?"
    stop music fadeout 1.5

    y "yo..."
    show monika forward lpoint happ om oe zorder 2 at t32
    show yuri turned pani om oe zorder 2 at h31

    m "okay, todo el mundo"

    y "..!"
    play music audio.t8
    m "ya es hora de compartir nuestros poemas, si esperamos más quizas no tengamos tiempo de comentarlos"

    show yuri turned lsur om ce zorder 2 at s31

    y "si por supuesto..."

    m forward neut om oe "¿te encuentras bien Yuri?"

    m "pareces decepcionada"
    show yuri turned pani om oe zorder 2 at h31
    y "no... todo bien"
    m forward lpoint happ om oe "Ok, todo el mundo empieza la ronda de compartir poemas"
    show monika neut om oe zorder 2 at thide 
    pause 1.2
    hide monika 
    "juraria que Monika me estaba mirando mal antes de irse"

    show yuri turned lsur om ce zorder 5 at s11
    "Yuri suelta el libro"

    mc "¿continuamos mañana?"

    y turned n1 happ cm oe "está bien aunque también podrias avanzar un poco en casa también me gustaria que disfrutes del libro y podamos compartir opiniones sobre el"

    mc "Mhmmm, que tal si lo avanzo en casa y continuamos leyendo juntos por donde lo deje mañana"

    y turned happ om ce "Me parece una magnifica idea"

    mc "Esta hecho"

    show yuri turned happ cm oe zorder 2 at thide
    hide yuri

    "me levanté para meter el libro dentro de mi mochila"

    with wiperight_scene
    show monika forward rhip happ om oe zorder 2 at t11
    m "[player] ¿escribiste el poema?"
    mc "fué mas dificil de lo que me esperaba pero si"
    m "No puedo esperar a leer lo que escribiste"
    mc "no tengas tantas expectativas jeje"
    m "Vamos, ten un poco más de confianza en ti mismo"
    mc "Jejeje... seguro"
    show monika forward rhip happ om oe zorder 2 at thide
    hide monika
    with wipeleft
    pause 0.8
    show sayori turned happ cm oe zorder 2 at t11
    "hasta ahora no habia pensado en lo vergonzoso que es esto, seguramente la unica critica constructiva que reciba sea de Sayori"
    show sayori turned happ cm oe zorder 2 at t21
    show natsuki cross neut om oe zorder 2 at t22
    "Estoy seguro que natsuki aplastara mi poema"
    show sayori turned happ cm oe zorder 2 at t31
    show natsuki cross neut om oe zorder 2 at t33
    show monika forward dist om oe zorder 2 at t32
    "Monika tratara de ser comprensiva pero sabre cuando este mintiendo"
    show sayori turned happ cm oe zorder 2 at t41
    show monika forward dist om oe zorder 2 at t43
    show natsuki cross neut om oe zorder 2 at t44
    show yuri turned neut cm oe zorder 2 at t42
    "Y Yuri...{w} Es la que más me tiene ansioso, como reaccionara al ver mi poema"
    show sayori turned happ cm oe zorder 2 at thide
    show monika forward dist om oe zorder 2 at thide
    show natsuki cross neut om oe zorder 2 at thide
    show yuri turned neut cm oe zorder 2 at thide
    hide monika 
    hide yuri 
    hide natsuki 
    hide sayori 
    "¡AAAAAAAAAH! Me va explotar la cabeza"
    stop audio fadeout 2.0
    "Calmate [player], puedes con esto"
    "Solo debes mostrar tu poema con una sonrisa y escuchar con atencion a las chicas"
    play music audio.t5
    show monika forward lpoint happ cm oe zorder 2 at t11
    m "bueno, ya que eres nuevo en el club elijes tu primero con quien compartir. "
    m lean "Quizas pueda ser yo"
    show sayori turned happ om oe zorder 2 at t41 
    s "monikaaa ¿quieres leer mi poema?"
    show monika forward happ om ce zorder 2 at f11
    m "ah... por supuesto Sayori"
    show monika forward happ om ce zorder 2 at thide
    show sayori turned happ om oe zorder 2 at thide
    hide monika 
    hide sayori 


    "Gracias Sayori, con el camino despejado"

    "Deberia enseñarle mi poema primero a Yuri...?"

    menu poema_yuri1:
        "Mostrar mi poema a yuri":
            "Si, deberia ir con Yuri"
            jump mostrar_poema_yuri
        "Quizás no":
            "Tal vez podria mostrarselo luego"
            jump mostrar_poema_natsukis


    
    with dissolve_scene_full 
    label mostrar_poema_yuri:
        play music audio.t5
        "con poema en mano me acerque a Yuri"
        show yuri turned mf e1d b1c zorder 2 at t11

        mc "¿te gustaria compartir poemas?"
        show yuri turned n2 flus cm oe zorder 2 at t11
        y "p-por supuesto"

        mc "sinceramente me da verguenza compartir un poema"

        y turned rup anno om oe "A-a mi tambien, nunca habia hecho algo parecido"

        mc "si quieres puedo empezar"

        y turned neut om oe "¿en serio?"

        y "N-no tienes por-{nw}"

        mc "no, no te preocupes quiero hacerlo"
        show yuri turned n1 lsur om ce zorder 2 at s11
        y "gracias"

        mc "por cierto dime si no entiendes mi letra..."

        "Yuri no mecionó nada, tomo mi poema y empezó a leerlo detenidamente"
        $ poem_db.show_poem("poem_mc1")
        #poner poema de MC
        show yuri turned happ om oe zorder 2 at h11
        y "Tu grafía es excelente y el poema es increible"

        mc "Vamos puedes ser sincera, es mi primera vez después de todo"

        y turned happ om ce "lo digo en serio de hecho no esperaba que lo hicieras tan bien"

        y turned laug cm oe "es como si hubiera sido creado para mi, el ambiente, el tono, La prosa. Me recuerda tanto a mis poemas"
        show yuri turned n2 ml e1b b2a zorder 2 at s11
        y "..."
        show yuri turned n2 nerv om oe zorder 2 at h11
        y "n-no intento decir que el poema va dirigido a mi... so-solo que me gustó mucho"

        mc "bueno quizas tengamos algo en comun"
        show yuri turned flus cm oe zorder 2 at s11
        y "uuuh..."

        y turned n1 lsur om oe "una pregunnta ¿alguna vez has escrito otros poemas?"

        y "A lo que me refiero es que la estructura de las rimas y la profundidad de las metáforas no reflejan el trabajo de un principiante."

        mc "muchas gracias por todos los halagos, signfican mucho para mi viniendo de ti, pero no"
    
        mc "es mi primera vez escribiendo poemas"
        mc "Digamos que estuve en eso toda la noche"
        mc "no queria decepcionarlas"
        y turned happ cm ce "Valio la pena todo el esfuerzo, es un gran poema"
        y turned n2 flus om oe "supongo que es mi momento..."

        show yuri turned n2 flus om oe zorder 2 at thide
        hide yuri

        "yuri busca el poema entre las paginas"

        show yuri turned lup rup worr om oe zorder 2 at s11

        "yuri dudando me pasó un cuaderno de notas, al mirarlo noto que hay otros poemas y no puedo evitar sentir curiosidad al verlos"

        $ poem_db.show_poem ("poem_mlb_yuri")

        show yuri turned shoc om oe zorder 2 at h11
    
        y "¡¡disculpa por la letra!! es horrible"

        mc "¿horrible? para mi es linda, parece que si tenemos algo en común después de todo, ambos escribimos en cursiva"

        y "oh... entonces por qué lo leiste mucho tiempo...?"

        mc "porque me gusta tu caligrafía y el poema esconde un mensaje"
        mc "Tuve que leerlo un par de veces para enterderlo del todo"

        show yuri turned n1 shoc cm ce zorder 2 at s11
 
        "yuri suspiro"

        y turned sad om oe "¿no es muy corto?"

        mc "no, de hecho creo que fue la manera perfecta de transmitir el mensaje"

        y turned ldown neut om oe "usualmente los suelo hacer mas largos..."

        mc "oye el tamaño no importa ¿verdad?"

        "¿verdad?"

        y turned happ om ce "me siento mas confiada al saber que te gustó"

        y turned laug om oe "y... mañana haré uno largo, en mi cuaderno también tengo algunos poemas"

        mc "Pude darme cuenta mientras buscabas tu poema"
        show yuri turned pani om oe zorder 2 at h11
        y "¿¡y-y l-los leistes!?"

        #añadie dialogo sobre lo que trate el poema, todavia no decidido
    
        mc "no, tranquila solo lei el que me entregaste"
        show yuri turned n2 flus cm oe zorder 2 at t11
        mc "pero seguramente son igual de buenos como el que me enseñaste"

        "Yuri con timidez buscaria una página especifica"
        $ poem_db. show_poem("poem_borr_yuri1")
        #añadir poema-borrador

        mc "vaya... si tengo mucho que aprender para poder escribir asi"
        show yuri turned n1 flus cm oe zorder 2 at f11
        y "¿a qu-que te refieres?"

        mc "eh, elegí mostrarte mi poema primero porque siento que eres muy buena en la creación de poemas"

        mc "y porque no me diras solo \"es muy bueno\" como alguien del club"
        show yuri turned n3 laug cm oe zorder 2 at t11
        "noté que yuri me miró avergonzada"

        mc "pero en fin... me gustaria aprender de ti"

        y turned laug cm oe "¿enserio piensas eso?"

        mc "estoy seguro que las demás también"
        show yuri turned rup lup lsur om oe zorder 2 at s11
        y "uh..."

        y turned ldown laug cm oe "sentía muchos nervios de hacer esto"

        y turned laug rdown cm ce "pero lo estoy disfrutando por ti"

        y "quiero hacerlo lo mejor posible por ti [player]"

        mc "ah..."

        mc "yo tambien..."

        y turned n1 happ cm oe "cuento contigo"

        mc "Vale, contigo ayudandome a mejorar puedo con todo"

        show yuri turned rdown happ cm oe zorder 2 at thide
        hide yuri

    with dissolve_scene_full
    play music audio.t5
    "Parece que termine de compartir mi poema con las chicas"
    "Cada poema tuvo distintos significados y todos bastante interesantes"
    show sayori turned happ cm oe zorder 2 at t11
    "\"Querido sol\", no creo que la mancha de chocolate caliente en la hoja sea una representacion de los sentimientos"
    show sayori turned happ cm oe zorder 2 at t21
    show natsuki turned neut cm oe zorder 2 at t22
    "el poema de Natsuki tuvo una moraleja que no me esperaba, puedes tratar y tratar pero no significa que lo lograras. me esperaba algo diferente..."
    show sayori turned happ cm oe zorder 2 at t31
    show monika forward lpoint happ cm oe zorder 2 at t32
    show natsuki turned neut cm oe zorder 2 at t33
    "y al final con Monika "

    "\"Hoyo en la pared\""

    "aunque lo lei 3 veces no entendi nada, ¿una epifania? no sabia que existia esa palabra"

    "por un momento sentí como si Monika solo siguiera hablandome por compromiso"

    "fué mas estresante de lo que creia, por lo menos me lleve consejos aunque era imposible superar los de ellas"

    "soy nuevo despues de todo"
    show sayori turned happ cm oe zorder 2 at thide
    show monika forward lpoint happ cm oe zorder 2 at thide
    show natsuki turned neut cm oe zorder 2 at thide
    hide sayori    
    hide monika 
    hide natsuki 
    pause 1

    "las chicas aun siguen intercambiando poemas"
    stop music fadeout 2.0
    "Parece que Sayori y Monika terminaron de compartir con todos"

    show yuri turned rup lup anno om oe zorder 2 at t21 
    show natsuki turned doub om oe zorder 2 at t22
    "Yuri y Natsuki parecen ser las unicas que faltan"

    "centré mi mirada en Yuri"

    show yuri turned anno om oe zorder 2 at t21
    "Yuri parece todo lo contrario a Natsuki, tranquila, calmada y paciente"
    
    "Mientras Natsuki es una bomba que en cualquier momento puede explotar"
    show natsuki turned pout om oe zorder 2 at t22
    n "(como es que leyeron esto)"

    "natsuki sostiene el poema con una de sus manos"

    show natsuki turned rhip pout cm oe zorder 2 at f22
    n "se podria decir que está bien"
    show natsuki turned rhip pout cm oe zorder 2 at t22

    show yuri turned neut om oe zorder 2 at f22
    y "muchas gracias... el tuyo es, lindo"
    show natsuki lhip vang cm ce zorder 2 at t22
    play music audio.t7
    n "¿lindo? estuviste leyendolo tanto tiempo y el unico comentario que se te ocurre es ¿está lindo?"

    show natsuki turned vang om ce zorder 2 at f22
    n "enserio ¿no pudiste comprender el obvio mensaje de que mas que intentes aveces no conseguiras lo que quieres?"
    show yuri turned anno om oe zorder 2 at f21
    show natsuki turned vang om ce zorder 2 at t22
    y "disculpa no creí que te ofenderia... intentaba hablar del lenguaje no que el poema sea infantil"
    show natsuki turned vang cm oe zorder 2 at f22
    show yuri turned anno om oe zorder 2 at t21
    n "¿¡Estas intentando vacilarme!?"
    show yuri turned doub om oe zorder 2 at f21
    show natsuki turned vang cm oe zorder 2 at t22
    y "bueno no fue malo más sin embargo puedo darte algunos consejos"
    show natsuki turned vang om oe zorder 2 at f22
    show yuri turned doub om oe zorder 2 at t21
    n "¿¡Consejos!?"

    n "¿¡Consejos de alguien que no le gustó mi poema!? ¡nunca los aceptaria!"

    n "y hay algunas personas a quien les gustó como Sayori, Monika"
    show natsuki turned vang om oe zorder 2 at f22
    n "y tambien [player] asi que dejame ser yo quien te de conse-{nw}"
    show yuri turned vang om ce zorder 2 at f21
    show natsuki turned vang cm oe zorder 2 at t22
    y "no necesito tus consejos Natsuki, he tenido años desarrollando mi estilo propio"

    y "además, no pienso en cambiarlo a menos que encuentre algo mucho mejor"
    show natsuki turned angr om oe zorder 2 at f22
    show yuri turned vang om ce zorder 2 at t21
    n "vaya no sabia que eras tan egocentrica Yu-{nw}"
    show yuri turned rup lup vang cm oe zorder 2 at f21
    show natsuki turned angr om oe zorder 2 at t22
    y "y tambien a [player] le gustó mi poema y el si acepto mis consejos"
    show natsuki turned angr om oe zorder 2 at f22
    show yuri turned rup lup vang cm oe zorder 2 at t21
    n "¡WOW!, como remarcaste a [player] creia que el era el unico que trataba de impresionar a alguien pero veo que tu tambien"

    y turned pani om oe "¡¡y-yo no trate de decir eso!!{w} lo que pasa es que estas celosa"

    show natsuki turned n3 shoc om oe zorder 2 at f22
    "natsuki intento hablar molesta pero fue interrumpida por Sayori"
    show natsuki turned n3 shoc om oe zorder 2 at t33
    show yuri turned rup lup vang cm oe zorder 2 at t31
    show sayori turned flus om oe zorder 2 at t32

    s "chicas está todo bien?"

    #aqui hablan nat y yu
    show natsuki turned vang cm oe zorder 2 at f33
    show yuri turned rup lup vang cm oe zorder 2 at f31
    show sayori turned pani om oe zorder 2 at s32
    ny "¡NO TE METAS!"
    show sayori turned pani om oe zorder 2 at thide
    hide sayori 
    show yuri turned rup lup vang cm oe zorder 2 at f21
    show natsuki turned vang cm oe zorder 2 at t22
    y "dijiste la unica..?"

    show yuri turned rup lup vang cm oe zorder 2 at t21

    show natsuki turned vang cm ce zorder 2 at f22
    n "gmhp"

    "natsuki colocó el poema en uno de los escritorios"

    "para luego levantarse firmemente "
    show natsuki cross vang cm ce zorder 2 at f22
    show yuri turned rup lup vang cm oe zorder 2 at t21
    n "por lo menos a mi no se me levantó el pecho inmediatamente que [player] entro al club"
    show yuri turned n3 pani om oe zorder 2 at h21
    show natsuki cross vang cm ce zorder 2 at t22
    y "¡N-n-natsuki!"
    show natsuki cross vang cm oe zorder 2 at t33
    show yuri turned n1 angr om oe zorder 2 at t32
    show monika forward rhip neut om oe zorder 2 at t31
    m "natsuki creo que no deberias de de-{nw}"

    #nat y yuri
    show natsuki cross vang cm oe zorder 2 at f33
    show yuri turned pani om oe zorder 2 at f32
    show monika forward rhip neut om oe zorder 2 at t31
    
    ny "¡ESTO NO TE INCUMBE!"

    show natsuki cross vang cm oe zorder 2 at t22
    show yuri turned pani om oe zorder 2 at t21
    show monika forward rdown sad om oe zorder 2 at thide
    hide monika

    y turned angr om ce "nunca haria algo tan v-vergonzoso... como tratar de hacer tierno todo!"

    "Parece que esta pelea esta escalando demasiado"

    "Tengo miedo de intervenir, no veo forma de parar este torbellino"

    "Como si el destino estuviera en mi contra ambas chican postran su mirada en mi"
    show yuri turned rdown flus cm oe zorder 2 at f21
    y "¡no le creas [player], Natsuki me está haciendo quedar mal!"

    y "J-jamas podría hacer eso"

    show natsuki turned vang om ce zorder 2 at t22
    show yuri turned n1 rdown flus cm oe zorder 2 at t21
    n "la unica que intenta hacer quedar mal a otra perosna eres tu yuri, tu empezaste todo esto"

    n turned angr om oe "¿verdad [player]?"
    show natsuki turned vang om ce zorder 2 at f22
    show yuri turned rdown flus cm oe zorder 2 at f21
    #ambas
    ny "Entonces!?"

    "..."

    "¿cómo es que todo pasó tan rapido?"

    "¿y porque se dirigen a mi?"

    "¿que deberia de hacer?"

    menu decision_ruta:
        "Hacerte el desentendido e intentar calmar las aguas.":
            "Es mejor que evite todo esto desastre"
            jump ruta_neutra_1
        

    #poner opciones por el momento se desarrolará la ruta neutral hasta el acto 2, este wei el jura

    #pretender que no estabas escuchando e intentar calmar la sitaucíon son opciones originales
    label ruta_neutra_1:
    "me levanté de mi asiento con un poco de miedo"

    mc "ambas son buenas escribi-{nw}"

    n cross n1 angr om ce "si ibas a dar una opinión tan mala mejor no hubieras dicho nada"

    "me senté rapidamente en mi asiento"

    y turned n1 angr om oe "natsuki no deberias de hablarle asi a [player] es una total falta de respeto"
    show natsuki turned angr om oe zorder 2 at f22
    show yuri turned angr om oe zorder 2 at t21
    n "S-silencio, Yuri"
    stop music fadeout 2.0
    n "sabes que pienso de ti, Yuri?"

    n turned angr om ce "al inicio pensaba que iba a ser increible tener una amiga con mis mismos gustos..."

    "natsuki se detuvo unos segundos"

    "Esta a punto de estallar la bomba"
    
    n turned vang om oe "¡pero ahora pienso que eres un perra engreida!"
    with vpunch
    show natsuki turned vang om oe zorder 2 at h22
    n "a nadie le sorprende que no tengas amigos"
    show yuri turned me e1g b1b zorder 2 at s21

    y "..."
    show natsuki sad om oe zorder 2 at s22
    pause 2
    show yuri turned cry cm ce zorder 2 at s21
    n "..."
    window hide
    show yuri shy sad om oe zorder 2 at t21
    pause 2
    show yuri shy sad om oe zorder 2 at correr_izquierda

    pause 0.4
    hide yuri 
    play audio closet_open
    window show
    "Yuri salió del club cubriendo sus ojos con una de sus mangas"

    "El club se queda en un silencio por un par de segundos"

    show natsuki turned fs cry om oe zorder 2 at t11


    "miro a Natsuki, parece arrepentida"

    n "yo.... ya regreso..."

    show natsuki turned fs cry cm ce zorder 2 at correr_izquierda
    pause 0.8
    hide natsuki 
    play audio closet_close
    "natsuki caminó hacia la puerta del salón y la cerro de un portazo, miré a Sayori"

    show sayori turned sad om oe zorder 2 at t11
    s "oh... se-seguramente todo se arreglará [player]"
    show monika forward sad om oe zorder 2 at t21
    show sayori turned sad om oe zorder 2 at t22
    m "si yo tambien pienso que estará todo bien, solo denles espacio"
    show monika forward sad om oe zorder 2 at thide
    show sayori turned sad om oe zorder 2 at thide
    hide sayori 
    hide monika 
    "tal vez pueda ayudar un poco en la situación"

    "caminé hacia la puerta del club pero senti como alguien me agarro del brazo"
    show monika forward anno om oe zorder 2 at f11
    m "[player] quedate aqui, soy la presidenta conozco a mis miembros asi que"

    m "confia en mi"
    show monika forward anno cm oe zorder 2 at t11
    mc "¿de qué hablas? deberiamos de intentar ayudarlas, no conozco lo suficiente a ambas pero..."
    mc "esa pele fue muy estúpida ¿pelear por el tema de un poema?"
    mc "solo les ganó el calor del momento"

    show monika lean anno om ce zorder 2 at f11
    m "como mencionas, a ellas no las conoces. Pero a mi sí"
    show monika lean anno om oe zorder 2 at f11
    "asi que, confia en mi"

    

    hide monika 
    with dissolve_scene_full

    #escena transición 
    play music audio.t5
    show monika forward lpoint happ om oe zorder 2 at f42
    show sayori turned happ cm oe zorder 2 at t43
    show yuri shy neut cm oe zorder 2 at t41
    show natsuki cross dist cm oe zorder 2 at t44
    m "¡okay, todo el mundo! ya es hora de irnos a casa, ¿qué tal les pareció la actividad?"
    show monika forward lpoint happ cm oe zorder 2 at t42
    show sayori turned happ om oe zorder 2 at f43
    s "¡me encanto!"
    show sayori turned happ cm oe zorder 2 at t43
    show yuri shy neut cm oe zorder 2 at s41
    y "..."
    show natsuki cross dist om oe zorder 2 at f44
    n "entretenido supongo"
    show natsuki cross dist cm oe zorder 2 at t44

    mc "supongo que estuvo bien"

    show monika forward lpoint happ om oe zorder 2 at t42

    m "¡muy bien!"

    m "mañana traigan un poema diferente y asi podremos aprender más de nosotros"

    show monika forward lpoint happ cm oe zorder 2 at t42

    show monika forward lpoint happ cm oe zorder 2 at thide
    show sayori turned happ cm oe zorder 2 at thide
    show yuri shy neut cm oe zorder 2 at thide
    show natsuki cross dist cm oe zorder 2 at thide
    hide sayori 
    hide monika 
    hide natsuki 
    hide yuri 

    "es cierto, gracias a la actividad pude saber que tipo de poemas le gustan a cada una"


    "quizas si hago un tipo de poema especifico pueda impresionar a Yuri"

    "siento la determinación en mi mismo"

    show sayori turned flus cm oe zorder 2 at s11

    s "¿[player]? holaa, tierra a [player]"

    mc "¿sayori?"

    show sayori turned happ om ce zorder 2 at f11
    s "hoy no creas que te escaparás de mi jeje"
    show sayori turned happ cm ce zorder 2 at t11
    "sayori me sonrie honestamente. Hace un tiempo ni si quiera hablabamos pero luce mas alegre desde que me uní"
    show sayori turned happ cm ce zorder 2 at thide
    hide sayori
    #transición ah esata weada donde salen casas
    scene bg street1_aft
    with wipeleft_scene
    show sayori turned dist cm oe zorder 2 at t11
    mc "sayori"
    show sayori turned neut om oe zorder 2 at t11
    mc "lo que ocurrió hoy en el club ¿Ocurre con frecuencia?"

    show sayori turned flus om oe zorder 2 at f11
    s "¿¡Eh!? ¿por supuesto que no!"

    show sayori turned nerv om oe zorder 2 at f11 
    s "nunca las habia visto pelear, de hecho son muy buenas amigas"

    s "no..."

    show sayori turned sad om oe zorder 2 at f11
    s"¿no las odias... o si?"
    show sayori turned sad cm oe zorder 2 at t11

    mc "no las odio, llevo dos dias en el club y me gustaria saber tu opinion"

    show sayori turned worr om oe zorder 2 at f11
    s "bueno, quizas hayan tenido un mal dia y por eso hayan reaccionado mal"
    show sayori turned worr om oe zorder 2 at s11
    s "espero no estés pensando en salirte..."
    show sayori turned worr cm oe zorder 2 at s11


    mc "¿no? aunque lleve poco tiempo me gusta estar en el club"

    show sayori turned happ om ce zorder 2 at f11
    s "me hace muuuuuy feliz que te guste estar en el club"

    s "¡además a todas les fascinas!"
    show sayori turned happ cm oe zorder 2 at t11

    "Sayori no piensa 2 segundos antes hablar"

    show sayori turned happ om oe zorder 2 at f11
    s "te prometo que cada dia será mejor"
    show sayori turned happ om oe zorder 2 at t11

    "suspiro"

    "sayori aún no entiende como me siento"

    mc "Espero todo mejore mañana"
    show sayori turned happ om oe zorder 2 at f11
    s "Todo estara bien, ya verás"
    show sayori turned happ cm oe zorder 2 at t11
    show sayori turned happ cm oe zorder 2 at thide
    hide sayori
    #cambio de escena a la casa de TN
    scene bg bedroom
    with wipeleft_scene
    stop music fadeout 1.0

    "hoy me siento mucho mas inspirado que ayer"

    "asi que un poema con simbolismo y una buena metrica"

    "Se me ocurren un par de ideas"

    "Los consejos de Monika estan dando sus frutos"

    stop music fadeout 1.0

    scene bg club_day
    with dissolve_scene_full
    play music audio.t8

    #cambio de escena de fondo abriendose para mostrar image (no se haga we)

    "llegué junto a Sayori al club"

    show sayori turned lup rup happ om ce zorder 2 at f11
    s "compartelos jeje~"  
    show sayori turned lup rup happ cm ce zorder 2 at thide
    hide sayori


    "como ayer, Natsuki está encerrada en el closet, Monika organizando papeles sobre el club"
    show yuri turned anno om oe zorder 2 at t11
    "y Yuri leyendo un libro, es difenrente al que leiamos ayer"

    "\"La anatomía del silencio\" murmuro, intentando descifrar la perturbadora ilustración de la portada."

    "Me pregunto cómo su cerebro puede procesar historias tan densas mientras toma té de lo más tranquila."

    #poner nombre de libro 
    show yuri turned happ cm oe zorder 2 at t11
    "me acerqué a Yuri, cuando me acerque a ella parecia un poco emocionada"

    show yuri turned happ om ce zorder 2 at f11
    y "ho-hola [player]"
    show yuri turned happ cm oe zorder 2 at t11

    mc "hola Yuri, disculpa no queria interrumpirte al leer"

    show yuri turned happ om oe zorder 2 at f11
    y "de hecho te estaba esperando para continuar"
    show yuri turned happ cm oe zorder 2 at t11

    "yuri aun estaba en la primera página"

    mc "ah entonces... ¿leemos?"

    show yuri turned happ om oe zorder 2 at f11
    y "por supuesto. Aunque primero me gustaria me gustaria hacer un poco de té ¿te parece bien?"
    show yuri turned happ cm oe zorder 2 at t11

    mc "me parece"

    show yuri turned rup happ om oe zorder 2 at f11
    y "si hay algo que mejore la lectura es una buena taza de té"
    show yuri turned rup happ om oe zorder 2 at s11
    y "(además de ti)"
    show yuri turned rup happ om oe zorder 2 at thide
    hide yuri 
    "yuri se levanto del asiento para dirigirse al closet, cuando regresa trae una jarra de agua"
    show yuri turned happ om oe zorder 2 at f11
    y "sostenlo porfavor"
    show yuri turned happ cm oe zorder 2 at t11

    "yuri me entregó la jarra junto a una tetera elecetrica"
    show yuri turned happ om oe zorder 2 at f11
    y "conectaré esto y luego necesitariamos un poco de agua"
    show yuri turned dist cm oe zorder 2 at s11
    "ella encendió la tetera elecetrica, Yuri es tan elegante incluso en sus movimientos"

    "yuri me pidió la jarra y se la entegué"

    show yuri turned happ om oe zorder 2 at f11
    y "ya regreso traeré agua"
    show yuri turned happ cm oe zorder 2 at t11

    mc "¿te puedo aconpañar?"

    show yuri turned laug om oe zorder 2 at f11 
    y "ah... bueno ¿porqué no?"

    show yuri turned n2 flus om oe zorder 2 at f11
    y "Esta bien, a-acompañame"

    show monika forward lpoint happ cm ce zorder 2 at t32

    show yuri turned n2 flus cm oe zorder 2 at t33

    "cuando iba a salir con Yuri de clases Monika se puso enfrente mio"


    mc "¿hola?"

    show monika forward lpoint happ om ce zorder 2 at f32

    m "¿a dónde van ustedes?"
    show monika forward lpoint happ cm ce zorder 2 at t32

    show yuri turned lup neut om oe zorder 2 at f33 
    y "vamos a llenar la jarra de agua, Monika"
    show yuri turned lup neut cm oe zorder 2 at t33
    show monika forward lpoint happ om oe zorder 2 at f32
    m "me parece bien, pero eso lo podria hacer una sola persona, ¿no?"
    show monika forward lpoint happ om oe zorder 2 at f32

    stop music fadeout 1.0

    m "y es u-{nw}"
    show yuri turned angr om oe zorder 2 at f33
    y "¿Monika puedes amablemente retirarte y dejarnos en paz?"

    y "o ¿te parece mal involucrar a [player] más que tu en las actividades del club?"

    show monika forward vsur om oe zorder 2 at f32
    m "¿eh?"

    mc "..."

    m forward ldown me e1b b1a "yo..."

    m "no hay nada de malo en eso"

    "yuri suspiró para luego salir rapidamente del club"

    play audio closet_open
    show yuri turned angr om oe zorder 2 at thide
    hide yuri  
    show monika forward neut cm oe zorder 2 at t11
    "acompañé a Yuri pero miré atras y vi a monika, me asusta un poco esa mirada"

    pause 1.0

    "rápidamente seguí el paso de Yuri"

    play audio closet_close

    pause 0.5

    scene bg corridor
    with wipeleft_scene
    play music audio.t9

    "yuri tenia la cara cubierta con sus manos"

    show yuri turned vsur om oe zorder 2 at f11

    y "l-lo dije sin pensar... como no pude pensar en que sonaría tan agresiva"

    show yuri turned vsur cm oe zorder 2 at t11

    mc "yuri..."

    show yuri turned vsur om oe zorder 2 at f11

    y "me molestó como Monika lo dijo... Pero no es justificación"

    y "¿será que al abrirme con los demas ya estoy mostrando lo insopotable que soy?"

    show yuri turned worr om oe zorder 2 at f11

    y "quizás debería de irme a mi casa..."

    show yuri turned lsur cm oe zorder 2 at t11

    mc "no yuri, no hiciste mal, no has hecho nada malo. pienso que lo has manejado bien"

    mc "no necesitas explicarle a otras personas lo que haces o no haces"

    mc "te culpas demasiado, incluso por cosas que no son tu culpa"

    show yuri turned anno om oe zorder 2 at f11

    y "porque..."

    show yuri turned vsur om ce zorder 2 at f11

    y "¿porqué eres tan amable conmigo?"

    show yuri turned worr cm oe zorder 2 at t11

    mc "porque nada lo de que haces es tan malo, nadie es perfecto. Todos cometemos errores"
   
    mc "incluyendome"

    mc "hay veces en la que pienso sin hablar, pero de todos modos ¿soy humano cierto?"

    mc "sobrepiensas mucho acerca de lo que dices"

    show yuri turned nerv cm oe zorder 2 at f11

    y "t-tu..."

    show yuri turned lsur om oe zorder 2 at f11

    y "¿porqué no me odias? incluso podria actuar terrible contigo..."

    show yuri turned lsur cm oe zorder 2 at t11

    mc "¿estás segura de eso ultimo?"

    show yuri turned sad om oe zorder 2 at f11

    y "no..."

    show yuri turned sad cm oe zorder 2 at t11

    mc "no puedo odiarte por expresarte de todos modos, los amigos siempre se apoyan"

    show yuri shy neut n5 m4 zorder 2 at f11

    y "¿¡am-amigo!?"

    y "m-me gusta que podamos... ¡qué podamos ser amigos!"

    show yuri shy neut n5 m1 zorder 2 at t11

    mc "gracias Yuri"

    "me pregunto como podré avanzar mas en esta relación, por el momennto me centraré en hacer que yuri se sienta mejor"

    show yuri shy neut n5 m1 zorder 2 at thide
    hide yuri
    stop music fadeout 1.5
    scene bg escaleras
    with dissolve_scene_full
    
    
    #cambio de escena a una tipo de escaleras o un lugar donde se encuentre un bebereo 

    show yuri turned neut n4 md e1c zorder 2 at t11

    "llegamos a la fuente de agua, yuri me estaba ayudando a llenar la jarra"

    "debido al acercamiento nuestras manos se sobreponian un poco"

    show yuri turned neut n4 mi e1c zorder 2 at f11

    y "[player] ¿piensas que Monika se haya molestado?"

    show yuri turned neut n4 md e1c zorder 2 at t11

    "vino a mi mente los ojos de monika"

    mc "no creo que Monika sea el tipo de persona que se enoja o que guarde rencor por algo tan..."

    mc "tan tonto"

    show yuri turned neut n4 mi e1d zorder 2 at f11

    y "quiero disculparme con ella"

    show yuri turned neut n4 md e1d zorder 2 at f11

    mc "me parece buena idea de hecho"

    show yuri turned neut n4 mi e1d zorder 2 at f11

    y "se que no soy buena expresandome... me gustaria mejorar en eso"

    y "algunas veces incluso me da miedo hablar con otras personas"

    show yuri turned neut n4 md e1d zorder 2 at t11

    y "..."

    show yuri turned curi om ce zorder 2 at f11
    
    y "la primera vez que te conocí sentí eso"

    show yuri turned laug cm oe zorder 2 at t11

    mc "¿enserio? ¿porqué?"

    show yuri turned worr om oe zorder 2 at f11

    y "en mi infancia, mis compañeros solían molestarme..."

    show yuri turned flus om oe zorder 2 at f11

    y "solia leer en receso y me veian raro por eso"

    show yuri turned lsur cm oe zorder 2 at t11

    mc "yuri, quizás no sea la persona mas amable pero sien-"

    show yuri turned shoc om oe zorder 2 at t11

    "senti como el agua de la jarra estaba mojando nuestras manos"

    "yuri mira la jarra y cerro la fuente"

    show yuri turned pani om oe zorder 2 at f11

    y "¡uuuu-!"

    y "el piso está mojado"

    y "pe-perdón"
    
    y "no estaba prestando atención de-de"

    y "e-es mi cu-"

    show yuri turned shoc cm oe zorder 2 at t11

    mc "yuri, está bien lo limpiaremos, juntos"

    "yuri aún parecia preocupada"

    show yuri turned lsur cm oe zorder 2 at t11

    mc "Yuri no hiciste nada malo"

    show yuri shy neut n4 m4 e3 b1 zorder 2 at f11

    y "pero por hablar demás se desbordó mucha agua en el suelo..."

    show yuri shy neut n4 m1 e3 b1 zorder 2 at t11

    mc "no hablo del agua, hablo de Monika, no debes de preocuparte por ello estoy seguro que Monika tambien te pedirá disculpas"

    mc "sé que solo llevo unos dias de conocerlas pero confia en ti, como yo lo hago en ti Yuri"

    show yuri shy neut n4 m4 e5 b2 zorder 2 at f11

    y "¿tu crees?"

    mc "estoy seguro, te lo prometo."
    
    mc "Prometo siempre ayudarte incluso en el más minimo problema"

    show yuri shy neut n4 m3 e3 b1 zorder 2 at t11

    y "..."

    "es un poco raro decirle esto a una chica que conozco hace media semana"
    
    "más sin embargo, si lo pienso"

    mc "asi que... ¿volvemos?"

    show yuri shy happ om oe zorder 2 at f11

    y "gracias [player]"

    y "volvamos al club probablemente se pregunten donde estamos"

    show yuri shy happ cm oe zorder 2 at f11

    "logré calmar la ansiedad de Yuri, siento que lo he manejado bien"

    #cambio de escena vuelta al club o incluso agregar escena en el pasillo (no muy preferible)

    scene bg club_day 
    with dissolve_scene_full

    play sound closet_open
    play music audio.tyuri

    "al entrar sentí las miradas de los demas miembros"

    show yuri turned rup curi om oe zorder 2 at f11

    y "¿conoces el té de oolong? es muy saludable y también ayuda a tener un mejor estado de animo"

    show yuri turned rup curi cm oe zorder 2 at t11

    mc "oolong suena como el nombre de un dragon mitlogico..."

    show yuri turned rup curi om oe zorder 2 at f11

    y "bueno un dia me gustaría enseñarte el arte de hacer un buen té"

    y "estoy segura que te gustará sobre todo beberlo"

    show yuri turned happ om ce zorder 2 at t11

    mc "es una buena idea de cita"

    show yuri turned lsur cm oe zorder 2 at t11

    y "...-"

    mc "y... ¿cuál es el primer paso para hacer té?"

    "intento cambiar de tema al ver la reacción de Yuri"

    with dissolve_scene_full
    show yuri lup lsur cm oe zorder 2 at thide
    scene bg club_day 

    "Yuri conectó la tetera electrica, aumentando la temperatura a 95 grados centigrados"

    show yuri turned lup rup mb e1a b1a zorder 2 at f11

    y "ahora se pone la tetera"

    show yuri turned lup rup ma e1d b1a zorder 2 at t11

    "yuri tomó la tetera y empezó a tomar las hojas de té"

    "para mi soprensa ella estuvo tarareando una canción"

    mc "¿disfrutas de hacer té no?"

    show yuri turned lup happ om oe zorder 2 at f11

    y "también, más sin embargo también pensaba en lo que te comenté antes"
    
    y "quiero expresarme mas con los demás, no es tan dificl como lo pensaba"

    show yuri turned laug om oe zorder 2 at f11

    y "por lo menos contigo"

    show yuri turned laug cm oe zorder 2 at t11

    y "..."

    show yuri turned flus om oe zorder 2 at t11

    y "cuando paso tiempo contigo me es más fácil expresarme"

    show yuri turned flus cm oe zorder 2 at t11
    
    mc "¡eso es muy bueno Yuri! solo no te sobreesfuerces"

    show yuri turned lup nerv om oe zorder 2 at f11

    y "siempre te procupas por mi..."

    show yuri turned lup lsur cm oe zorder 2 at f11

    y "es muy lindo de tu parte"

    show yuri turned lup lsur cm ce zorder 2 at f11

    "espera necesito un respiro de esto"

    scene bg club_day
    with dissolve_scene_full

    "Yuri pone dos tazas para cada uno"

    show yuri turned rup happ om oe zorder 2 at f11

    y "¿te gustaria leer en el suelo hoy?"

    show yuri turned rup happ cm oe zorder 2 at t11

    mc "¿está bien? pero ¿porqué?"

    show yuri turned rup happ om oe zorder 2 at f11

    y "se lee mejor con la espalda apoyada en la pared"

    show yuri turned rup happ cm oe zorder 2 at f11

    mc "oh, disculpa, ahora que lo pienso si es un poco incomodo leer con las sillas"

    show yuri turned happ om oe zorder 2 at f11

    y "tranquilo, casi siempre tengo dolores de espalda asi que puedo soportarlo"

    y "es por mi-"

    show yuri turned pani om oe zorder 2 at f11

    y "ah...-!"

    show yuri turned lup rup pani cm ce zorder 2 at f11
    pause 0.5
    show yuri turned rup pani om oe zorder 2 at f11
    pause 0.5
    show yuri turned pani cm ce zorder 2 at f11
    pause 0.5
    show yuri shy neut n5 m2 zorder 2 at f11


    mc "tu postura al leer... ¿cierto?"

    show yuri shy neut n3 m4 e2 b1 zorder 2 at f11

    y "s-si es eso"

    show yuri shy neut n3 m2 e1 b1 zorder 2 at t11

    "no creo que haya sido eso, pero prefiero no indagar en el tema"

    show yuri shy neut n3 m4 e1 b1 zorder 2 at t11

    mc "te encorvas mucho al leer supongo"

    show yuri turned nerv om oe zorder 2 at f11

    y "¡si! tengo una terrible postura"

    hide Yuri
    scene y_cg2_bg1
    show y_cg2_dust1
    show y_cg2_base
    show y_cg2_nochoc
    with dissolve_scene_full



    "nos sentamos en una de las paredes cerca de la ventana"

    "sostengo con una de mis manos el libro Yuri hace lo mismo de la parte contraria"

    "sentí que no podia respirar cuando Yuri choco su hombro con el mio"

    #empezar a leer el libro que todavia no esta definido si saldra o si debemos de cambiar algo, en dado caso si existe poner escena del libro
    y "[player] ten"

    "Yuri me pasó una taza de té"

    mc "gracias Yuri"

    "Realmente estamos mas cerca de lo que esperaba, puedo escuchar su respiración"

    show y_cg2_exp3

    #libro

    mc "oh, se me había olvidado"

    "saque una pequeña bolsa de mis bolsillos"

    mc "Sayori me habia dado unos chocolates y creo que es una buena ocasión para comerlos"

    mc "creo que el chocolate con té sabrá bien ¿no?"

    y "¿chocolate?"

    mc "si, ten"

    "Yuri intento agarrar el chocolate pero debido a la postura era muy dificil sin hacerlo incómodo"

    y "[player] no puedo agarrar los chocolates sin que el libro se caiga"

    "dudé unos segundos en seguir mis pensamientos"

    mc "entonces... ¿asi está bien?"

    y "..."

    "Levanté el choclate hacia Yuri"

    "Yuri se inclinó lentamente mordiendo el chocolate, nuestras miradas se cruzaron"

    "pero no es un momento incomodo, es más tranquilo..."

    "aparte la mirada"

    y "es-eso..."

    m "¡okay todo el mundo!"

    mc "¿¡EEEH!?"

    "por el susto terminé ahogandome con el chocolate"

    scene bg club_day
    show yuri turned shoc om oe zorder 2 at f11

    y "¡[player]!"

    with wipeleft_scene 

    #añadir escena de transición

    show yuri turned shoc cm oe zorder 2 at t11

    mc "cof cof"

    show yuri turned shoc cm oe zorder 2 at t21
    show monika forward rhip anno om oe zorder 2 at f22

    m "disculpen no pensaba en asustarlos, me imagino que habrán estado muy concentrados"

    show monika forward happ cm oe zorder 2 at t22

    mc "menos mal aun quedaba un poco de té"

    show yuri turned dist cm oe zorder 2 at t21

    "Terminé de beber toda la taza de té."

    show monika forward lpoint neut om oe zorder 2 at f22

    m "uh... es tiempo de compartis poemas chicos"

    show monika forward lpoint neut om ce zorder 2 at f22

    m "porcierto debido al tiempo Yuri te sugiero que guardes las cosas de té"

    show yuri turned dist om oe zorder 2 at t21

    y "está bien"

    "Yuri aun parecia un tanto preocupada asi que me acerque para ayudarle a guardar el juego de té"
    show yuri turned dist om oe zorder 2 at t21
    hide yuri

    show monika forward lpoint neut om ce zorder 2 at f22
    hide monika

    with wipeleft_scene 

    "luego de terminar de limpiar, era momento de compartir mi poemas "
    
    "aunque no se si sea buena idea compartirlo con Yuri... por lo que paso hace unos minutos..."

    "espero no lo tome a mal..."

    menu poema_yuri2:
        "Mostar mi poema a Yuri":
            "Estoy seguro que a ella también le gustó pasar tiempo conmigo"
            jump mostrar_poema_yuri
        "Quizás no...":
            "Creo que seria mejor hacerlo después cuando todo esté mas tranquilo"
            jump mostrar_poema_Sayori

    #añadir eleccion de poemas a Yuri (pensar si serviria esto)
    ######################POEMA DE YURI AQUI
    label mostrar_poema_yuri2:

        play music audio.t5

        "me acerqué a Yuri"

        show yuri turned happ cm oe zorder 2 at t11

        mc "¿lista?"

        show yuri turned happ om oe zorder 2 at f11

        y "por su puesto, quiero ver como seguiste mis consejos"

        show yuri turned happ cm oe zorder 2 at f11

        "espero no me destruya..."

        "alze mi mano para darle el poema a Yuri"

        #añadir poema 

        show yuri turned neut om oe zorder 2 at f11

        y "[player]..."

        show yuri turned neut cm oe zorder 2 at t11

        mc "¿s-si?"

        "siento que va a notar que lo escribí en la noche... Supongo que no vale la pena sobrepensar, eso no soluciona nada"
    
        #añadir escena de interrumpir dependiendo de la reescritura 

        show yuri turned happ om ce zorder 2 at f11

        y " Me gustó mucho más que el de ayer"

        show yuri turned happ cm ce zorder 2 at t11

        "¿qué?"

        show yuri mb e1d zorder 2 at f11

        y "añadiste muy bien el simbolismo y esta vez intentaste algo nuevo, experimentaste y realmente te salió bien"

        show yuri turned laug om oe zorder 2 at f11

        y "si sigues mejorando puedes incluso podrias ser el mejor escritor del club, yo lo creo"

        show yuri turned laug cm oe zorder 2 at f11

        mc "no creo que sea tan bueno como mencionas Yuri, pero si seguí tus consejos y además lei algunos libros"

        show yuri turned nerv om oe zorder 2 at f11

        y "tu poema es tan impresionante... ¿t-te importaria si me lo quedo?"

        show yuri turned lsur cm oe zorder 2 at t11

        mc "pero aun tengo que compartilo Yuri..."

        show yuri turned worr cm oe zorder 2 at t11

        mc "pero no tengo problemas"

        show yuri turned laug om oe zorder 2 at t11

        "yuri me sonrio ligeramente, espero no se lo tome a mal"

        show yuri turned flus om oe zorder 2 at f11

        y "con mas práctica podrías incluso expresar tus sentimientos o como te sientes yo... aveces lo hago"

        show yuri turned rup laug cm oe zorder 2 at t11

        mc "seria muy dificil escribir mis pensamientos"

        show yuri turned curi om oe zorder 2 at f11

        y "¿a qué te refieres?"

        show yuri turned curi cm oe zorder 2 at t11

        mc "no me sentiría tan comodo describiendome a los demas"

        mc "e incluso creo que incomodaria a los demás miembros haciendolo"

        show yuri turned happ om oe zorder 2 at f11

        y "bueno no tiene que ser a todos puede ser con alguien especial"

        show yuri turned happ om oe zorder 2 at s11

        y "como yo..."

        show yuri turned laug cm oe zorder 2 at t11

        mc "suena a una buena idea para mi proximo poema"

        "Yuri me paso su poema. Era una hoja suelta"
        $ poem_db.show_poem("Yuri_poem2")
        show yuri turned laug cm oe zorder 2 at thide
        hide yuri

        with wipeleft_scene 
        jump pelea

    #añadir poema 

    #añadir escena del poema, salto final de escena 

    label pelea:

        play music audio.t5

    "¿enserio terminé de compartir mi poema con las demas? ellas aun  siguen compartiendo opiniones"

    "fué muy notable como mejoraron todas sus poemas, el que más me sorprendió fué el de Sayori" #aqui poner un poco mas de textos sobre los podemas de Yuri, MOnika y Natsuki

    "ese poema me dejó pensando luego de leerlo..."

    "me senté en uno de los pupitres"

    "mis ojos se centra en Yuri, ella está compartiendo su poema con Monika aunque parece mas timida de lo normal"
    

    show yuri turned flus om oe zorder 2 at t21
    show monika forward rhip anno cm oe zorder 2 at t22

    stop music fadeout 1.5

    "luce como si pidiera perdón por algo"

    show yuri shy angr cm oe zorder 2 at t21
    show monika forward rhip anno om oe zorder 2 at f22

    m "¿entendido?"

    show yuri shy angr om oe zorder 2 at f21
    show monika forward rhip anno cm oe zorder 2 at f22

    y "s-si..."

    show yuri shy angr om oe zorder 2 at thide
    hide Yuri
    show monika forward rhip anno cm oe zorder 2 at thide
    hide monika


    "yuri asintió con la cabeza"

    "¿será algo importante?"

    "parecía muy triste o indiferente... Qué será lo que estab-"

    show monika forward lpoint rhip happ om oe zorder 2 at f11

    m "¡okay todo mundo!"

    show monika forward lpoint rhip happ om ce zorder 2 at f11

    m "con esto se concluye el compartir de poemas"

    show sayori turned lup neut om oe zorder 2 at f11
    show monika forward rhip happ cm oe zorder 2 at f21

    s "Monika me tendré que ir temprano nos vemos mañana"

    show sayori turned lup neut om ce zorder 2 at f11
    show monika forward rhip happ cm oe zorder 2 at f21

    s "adiositiooo"

    show sayori turned lup neut om ce zorder 2 at thide
    hide sayori
    show natsuki cross dist om oe zorder 2 at f21
    show monika forward rhip happ cm oe zorder 2 at t21

    n "si yo también mi padre me está esperando"

    show natsuki cross dist om oe zorder 2 at thide
    hide natsuki
    show monika forward rhip happ cm ce zorder 2 at f21

    m "bueno, cuidense hasta mañana"

    show monika forward rhip happ cm ce zorder 2 at thide
    hide monika

    "solo quedamos yo, yuri y monika en el club, quizas pueda decirle si me acompaña a irme a casa"

    show yuri turned dist cm oe zorder 2 at t11

    mc "oye yuri ¿quie-"

    show yuri turned pani om oe zorder 2 at f11

    y "¡ahh!"

    show yuri turned sad om oe zorder 2 at f11

    y "¡disculpa [player] me tengo que ir!"

    show yuri turned sad om oe zorder 2 at thide
    hide yuri

    "yuri salió rapidamente del club sin siquiera voltearme a ver"

    "definitivamente ha pasado algo con ella, esta actuando raro quizas Monika sepa algo"

    "Monika estaba sentada en el escritorio junto a una computadora"

    "quizas la interrumpa... Pero Yuri es mi prioridad"

    show monika forward happ om oe zorder 2 at f11

    m "oh, ¡hola [player]! ¿necesitas algo?"

    show monika forward happ cm oe zorder 2 at t11

    mc "si ¿has notado que Yuri ha estado un poco rara luego de..."

    show monika forward flus om oe zorder 2 at f11

    m "bueno quizas deberías de ignorarla"

    show monika forward flus cm oe zorder 2 at t11

    mc "¿disculpa?"

    show monika forward worr om oe zorder 2 at f11

    m "quizás me di a mal entender, me refiero a que Yuri no habla frecuentemente con nosotros o tras personas"

    m "es más solitaria incluso en el club"

    show monika forward worr cm oe zorder 2 at t11

    "La expresión de Monika cambia al ver la mia"

    show monika forward nerv om oe zorder 2 at f11

    m "no me refiero a que no le hables, solo que es mejor tener una pequeña charla con ella y dejarla sola"

    show monika forward happ om ce zorder 2 at f11

    m "creeme conozco perfectamente a mis miembros"

    show monika forward dist cm oe zorder 2 at t11

    mc "pensaba que nos llevabamos bien en realidad"

    show monika forward neut om oe zorder 2 at f11

    m "Yuri puede ser un poco obsesiva con algunas cosas..."

    show monika forward neut cm oe zorder 2 at f11

    "¿obsesiva? quizas si tenga un poco de razón... Ella suele disculparse mucho incluso por lo minimo"

    mc "¿obsesiva en?"

    show monika forward worr om ce zorder 2 at t11

    "Monika suspiró"

    show monika forward anno lpoint om oe zorder 2 at f11

    m "mira [player] solo no estes tanto tiempo con Yuri, además también puedes pasar tiempo con las demás"

    show monika forward rhip happ om oe zorder 2 at f11

    m "como yo"

    show monika forward rhip happ cm oe zorder 2 at t11

    "¿qué me está intentando decir? Monika la presidenta del club ¿me está pidiendo que pase el tiempo con ella?"

    show monika lean happ cm oe zorder 2 at t11

    mc "digo... pensaba que Yuri y yo nos llevabamos bien"

    show monika lean anno cm oe zorder 2 at f11
    pause 1.0
    show monika lean neut om oe zorder 2 at f11

    m "realmente no conoces a Yuri"

    show monika lean anno om oe zorder 2 at t11

    mc "quizás solo llevo unos dias hablando con ella, pero cada dia intento aprender más de ella"

    "me detuve unos segundos para formular mi pregunta"

    show monika forward vsur cm oe zorder 2 at t11

    mc "vi que le dijiste algo a Yuri hace un rato"

    show monika forward nerv cm oe zorder 2 at f11

    m "¿enserio?"

    show monika forward nerv cm oe zorder 2 at t11

    mc "si recuerdo que le susurraste y-"

    show monika forward laug om oe zorder 2 at f11

    m "oh... tranquilo es una cosa entre nosotras, ya sabes cosas de chicas"

    show monika forward laug cm oe zorder 2 at t11

    "siento que me esta mintiendo"

    mc "..."

    show monika forward laug om oe zorder 2 at f11

    m "bueno tengo unas cosas que hacer, asi que nos vemos mañana [player]"

    show monika forward laug cm oe zorder 2 at r11

    "que manera tan amable de decir, largate"

    show monika forward worr cm oe zorder 2 at t11

    mc "esta bien, adios Monika"

    #cambiar a escena de casa de TN
    scene bg club_day
    with dissolve_scene_full
    scene bg kitchen

    "cosas de chicas"

    "aún recuerdo su cara parecia una mezcla de ansiedad y miedo"

    "y solo me ignoro para irse del club..."

    "mañana deberia de preguntarle... obsesiva... obsesión..."

    "creo que ya tengo la suficiente inspiración para poder escribir otro poema"

    "no pienso que ella la este pasando mal conmigo... cada dia la entiendo mejor"

    "yo también me he abierto a ella"

    "pero Monika..."

    mc "..."

    mc "no estoy llegando a ni un punto"

    scene bg kitchen
    with dissolve_scene_full
    scene bg corridor

    #transición

    "realmente no me interesa si a Monika le parece bien o mal que hablemos"

    "aunque siento que hay algo más... más..."

    #transición

    "antes de abrir la puerta del club escuche como se elevaba la vos adentro"

    mc "que..."

    "abrí la puerta"
    scene bg corridor
    with dissolve_scene_full
    play sound closet_open
    scene bg club_day

    #transicion

    show yuri turned pani om oe zorder 2 at h11
    show monika forward anno cm oe zorder 2 at t21

    y "perdoname Monika no intentaba faltarte al res-"

    show yuri turned lsur cm oe zorder 2 at t11
    show monika forward anno om oe zorder 2 at f21

    m "no acepto tus disculpas Yuri"

    show yuri turned lsur cm oe zorder 2 at t11
    show monika forward anno om ce zorder 2 at f21

    m "desde que estas en el club has sido igual de tóxica"

    show yuri turned lsur cm oe zorder 2 at t11
    show monika forward angr om ce zorder 2 at f21

    m "ni siquiera te comunicas con nosotras, vienes lees tus estúpidos libros y te vas"

    show yuri turned dist cm oe zorder 2 at t11
    show monika forward angr om ce zorder 2 at f21

    m "¡si sabes que existen las bibliotecas Yuri!"

    show yuri turned lup angr cm oe zorder 2 at f11
    show monika forward angr cm oe zorder 2 at t21

    "Yuri apretó su mano como si intentara decir algo"

    show yuri turned lup angr cm oe zorder 2 at t11
    show monika forward anno om oe zorder 2 at f21

    m "¿qué? ¿quieres decir algo?"

    show yuri turned lup anno om oe zorder 2 at f11
    show monika forward anno cm oe zorder 2 at t21

    y "y-yo...."

    show yuri turned lup vang cm oe zorder 2 at f22
    show monika forward anno cm oe zorder 2 at t21

    y "pienso que eres una maldita egocentrica"

    show yuri turned lup vang cm ce zorder 2 at f22
    show monika forward pout cm oe zorder 2 at t21

    y "¿enserio piensas que está bien tratar como un estorbo a un miembro de tu club?"

    show yuri turned lup vang cm ce zorder 2 at f22

    y "te crees que eres la mejor solo por ser popular cuando en realidad eres una puta narcisista"

    show yuri turned lup vang cm oe zorder 2 at f22

    y "con el ego mas frágil que una rosa"

    show yuri turned lup yand cm ce zorder 2 at f22

    y "asi que... ¡piensa dos veces antes de hablar!"

    show yuri turned lup yand om ce zorder 2 at f22

    y "porque cuando acabe contigo, ni si quiera tus padres podran reconocer-"

    show yuri turned yand cm ce zorder 2 at t22
    show monika forward sedu om oe zorder 2 at f21

    m "que si Yuri, que si"

    show yuri turned yand cm ce zorder 2 at t22
    show monika forward lpoint sedu om ce zorder 2 at f21


    m "¿porqué no muestras a los demás como realmente eres?"

    show yuri turned yand cm ce zorder 2 at t22
    show monika forward lpoint sedu cm oe zorder 2 at t21

    "Monika voltea a verme, ella ya sabía que estaba aquí"

    show yuri turned yand om ce zorder 2 at t22
    show monika forward lpoint rhip sedu cm oe zorder 2 at f21

    m "vamos, muestrale a [player] como realmente eres"

    show yuri turned shoc cm oe zorder 2 at h22
    show monika forward lpoint rhip sedu cm oe zorder 2 at t21

    "Yuri se da cuentan de mi presencia"

    show yuri turned shoc om oe zorder 2 at f22
    show monika forward lpoint rhip sedu cm oe zorder 2 at t21

    y "¿[player]...? N-no espera, no intentaba decir eso!"

    show yuri turned cry om ce zorder 2 at f22

    y "¡No soy asi!"

    show yuri turned cry om oe zorder 2 at f22

    y "y-yo solo..."

    show yuri turned cry cm oe zorder 2 at t22

    "monika le tocó el hombro a Yuri haciendo que ella la voltee a ver"

    show monika forward happ om oe zorder 2 at f21

    m "tranquila, siempre puedes tener un consejo de mi parte incluso en los momentos malos"

    show monika forward happ om ce zorder 2 at f21

    m "¿has considerado acabar con tu vida?"

    show monika forward flus om oe zorder 2 at f21

    m "¡ayudaria a que dejes de hacer esas cosas!"
    show yuri turned cry cm oe zorder 2 at t22
    show monika forward flus cm oe zorder 2 at f21

    y "..."
    show yuri turned cry cm oe zorder 2 at thide
    hide yuri 
    show monika forward flus cm oe zorder 2 at thide
    hide monika 

    "como ayer, Yuri salio de la habitación no tenia los ojosn llorosos"
    
    "Ella estaba llorando, estoy asustado por las plabaras de Monika"

    "realmente no se que decir"
    
    "..."

    "iré a ver a Yuri, cuando iba a salir del club Monika me detuvo"

    show monika forward lpoint worr om oe zorder 2 at f11

    m "oye, dejala ella necesita estar sola pa-"

    show monika forward vsur cm oe zorder 2 at t11

    mc "que mierda pasa contigo Monika. Un consejo, matate. ¿en serio?"

    "noto a mi alrededor, Sayori esta en una silla curbriendose los oidos con sus manos"

    "ella"

    "está sollozando"

    show monika forward anno om oe zorder 2 at f11

    m "oh bueno gritame y hazme ver como la mala"

    show monika lean anno om oe zorder 2 at f11

    m "ya has visto como es Yuri, solo me defendí frente a lo que me dijo"

    show monika lean angr cm oe zorder 2 at t11

    mc "estas enferma... Yuri no es asi sacaste su peor lado, ire con ella"

    show monika forward neut om oe zorder 2 at f11

    m "espera"

    show monika forward neut cm oe zorder 2 at t11

    "no me detuve y abri la puerta"

    show monika forward neut om oe zorder 2 at f11

    m "lo digo enserio, no creo que te guste lo que estas aputno de ver"

    show monika forward neut cm oe zorder 2 at f11

    mc "callate maldita insoportable"

    scene bg escaleras
    with dissolve_scene_full
    
    #transición 

    "intente seguir el ritmo de Yuri pero ella corria demasiado rapido"

    #transicioón 

    "cuando bajaba las escalera termine cayendo en el suelo golpeandome la cabeza"

    mc "mierda..."

    "intente levantarme con dificultad, ha este punto probablementer Yuri ya se haya ido"

    "me sostuvo de una parte de las escalera, logré esuchcar unos sollozos cercanos en el silecioso pasillo"

    "seguí el sonido de los sollozos, venian del baño"

    "es el baño de las mujeres dudo que pueda entrar..."

    "prefiero que me expulsen antes que dejar sola a Yuri!"


    show yuri turned lup rup cry om oe zorder 2 at t11
    mc "¡Yuri esperame!"
    show yuri turned lup rup cry om oe zorder 2 at thide
    hide yuri 
    "intenté seguirla pero terminé resbalandome y golpeandome la cabeza"
    mc "¡agh!..."
    "me levanté rápidamente, aunque intente seguir el ritmo no pude"

    with dissolve_scene_full

    #añadir escena prespectiva de Yuri 
    play music audio.t10 fadein 2.0
    with dissolve_scene_full
    scene bg bano_Yuri_nocuchillo
    "???" "¿No crees que deberías deja de huir de huir de tus problemas?"
    show yuri_pequena_seria zorder 2 at f11
    "(yuri)" "si creo que sería la mejor idea"
    show yuri_pequena_seria zorder 2 at thide
    hide yuri_pequena_seria
    show yuri_pequena_neut zorder 2 at t11
    y "[player] m-me vio actuando asi... E-el va despreciarme... soy una fenomeno"
    show yuri_pequena_neut zorder 2 at thide
    hide yuri_pequena_neut 
    show yuri_pequena_tired zorder 2 at f11
    "(yuri)" "El no te odia, solo estará un poco sorprendido..."
    show yuri_pequena_tired zorder 2 at thide
    hide yuri_pequena_tired
    show yuri_pequena_neut zorder 2 at t11
    y "No puedo soportarlo más... Monika, Monika"
    show yuri_pequena_neut zorder 2 at t11
    hide yuri_pequena_neut
    show yuri_pequena_sad2 zorder 2 at f11
    "(yuri)" "yuri espera creo que deberias... ¡N-no! ¡espera!"
    show yuri_pequena_sad2 zorder 2 at thide
    hide yuri_pequena_sad2
    with dissolve_scene_full
    scene bg bano_Yuri_nocuchillo

    ############################

    mc "yu-yuri?"

    scene bg bano_Yuri
    show yuri_sentada zorder 2 at t11:
        xalign 0.3

    y "-!"

    "no pude evitar mirar el brazo de Yuri"

    "tiene tantas marcas de cortes... algunas recientes... otras no"


    y "[player] n-no se supone que deberia de estar aqui..."

    "no tengo la suficiente fuerza para decir algo, di unos pasos para poderme acercar"

    y "¡No!"

    y "alejate... porfavor..."

    y "soy peor que un fenómeno..."

    "Yuri apreto su mano derecha y volvió a cortarse"

    mc "por-porfavor... Yo solo quiero ayudarte"

    mc "estas sangrando mucho... quizas te puedan atender en la enfermeria, yo te llevaré..."

    y "yo... no merezco ser ayudada, no quiero tu ayuda, me esuchaste... esuchaste como soy realmente"

    y "tan"

    y "desagradable"

    "volvi a acercarme a ella"

    "se que Yuri también estuvo mal diciendo eso... pero fue por la insensibilidad de Monika"

    mc "no puedo juzgarte Yuri..."

    "por unos segundos nuestras miradas chocaron"

    "sus ojos lavanda se tiñieron de lagrimas que no dejaban de salir"

    "su expresión era completamente diferente... era de desesperación"

    y "hay tantas emociones... Que las he guardado por tanto tiempo... Tantoa años"

    y "por si fuera poco no puedo contenerlas..."

    hide yuri_sentada

    #show yuri_parada zorder 2 at t11 este sprite le falta

    "Yuri se levantó del suelo al ver como me acerco a ella"

    y "¡alejate de mi!"

    "no se que hacer... pero haré todo lo que pueda"

    "para ayudarla"

    mc "Yuri... Escuchame porfavor, yo realmente quiero te quiero ayudar no me importa lo que le dijiste a Monika"

    mc "yo quiero, no me importa tu pasado. Me importas tu Yuri por eso me encuentro aqui ahora"

    mc "intentandolo..."

    "sus gotas de sangre cayeron en el suelo poco a poco mientras ella se volteba evitando verme"

    "no sé como acabe esto... Pero haré lo que sea con tal que Yuri esté bien"

    y "¡ya te dije que no quiero tu ayuda!"

    y "no se si un dia no pueda controlarme y termine haciendo daño a los demas... haciendote daño a ti"

    y "no puedo luchar con esto, no lo puedo controlar, soy un titere de mis sentimiento..."

    y "no puedo dejar que los demás vean como realmente soy..."

    y "yo no quiero aceptar quien realmente soy... porque se que solo soy"

    y "una maldita enferma"

    "mientras Yuri hablaba lentamente me acerqué a ella"

    y "¡escuchame, no merezco ser ayudada mucho menos por ti!"

    y "¡¡¡¡SOLO DÉJAME EN PAZ!!!!"

    "logré estar cerca de ella e intenté agarrar sus manos"

    "por unos segundos lo logré, Yuri parecía mas calmada"

    mc "Yuri, todo va a estat bien... Estoy seguro que no solo yo quiero lo mejor para ti"

    mc "también Natsuki, Sayori..."

    y "monika... L-lo siento"

    #show yuri_parada zorder 2 at t11
    #hide yuri_parada

    mc "¡Yuri espera!"
    stop music fadeout 2.0

    #transición
    with dissolve_scene_full
    scene corridor

    "aunque intente alcanzarla, el dolor en mi cabeza incrementaba por los movimientos bruscos"

    "la he perdido..."

    "casi nuna he visitado mucho los pasillos, aunque lleve un tiempo no conozco todos los lugares"

    mc "Yuri... dejame ayudarte"

    "me senté en una banca y lleve mis manos a mi cara"

    "mientras descanso siento como si mi cabeza estuviera por explotar"

    "no puedo quedarme aqui sin hacer nada"

    "me levante y empecé a caminar con un poco de dificultad"

    "pestañé y de un momento a otro me había chocado con una pequeña figura"

    mc "¡auch!"

    "unas monedas cayeron en el suelo luego del golpe repentino"

    play music audio.t6 fadein 1.5

    show natsuki turned lhip rhip ff angr om oe zorder 2 at f11

    n "las monedas... idiota fijate por donde vas"

    show natsuki turned rhip ff anno cm oe zorder 2 at t11

    mc "¿Natsuki? disculpa Natsuki no te habia visto"

    show natsuki turned rhip ff anno om oe zorder 2 at f11

    n "de que hablas si por poco pasasbas atropellandome ¿de casualidad no estas borracho?"

    n "la próxima no te perdonaré"

    show natsuki turned ff curi cm oe zorder 2 at t11

    mc "ya pedí perdon Nat- y esas monedas son tuyas, ¿verdad?"

    show natsuki turned lhip rhip ff angr om oe zorder 2 at f11

    n "¡que te importa!"

    show natsuki turned ff worr cm oe zorder 2 at t11

    mc "esta bien disculpa..."

    show natsuki turned ff dist cm oe zorder 2 at t11

    "Natsuki observa las monedas en el suelo para luego voltear a ver"

    pause 1.0

    show natsuki turned lhip ff sad om oe zorder 2 at f11

    n "está bien losiento, estaba buscando algunas monedas para ayudar a mi padre con su trabajo"

    n "aunque sea solo unas monedas ayuda mas de lo que parece"

    show natsuki turned ff sad cm oe zorder 2 at t11

    mc "oh..."

    show natsuki turned ff sad om ce zorder 2 at t11

    "ambos estuvimos en silencio ¿porqué hoy parece que todos estan mal?"

    "o en realidad... hoy me doy cuenta de quienes estan mal"

    show natsuki turned ff dist om oe zorder 2 at f11

    n "ugh, ya solo olvidalo"

    show natsuki turned ff curi om oe zorder 2 at f11
    
    n "porcierto ¿porqué no estas en el club?"

    show natsuki turned ff neut cm oe zorder 2 at f11

    mc "bueno es un poco dificil de explicar pero necesito encontrar a Yuri"

    show natsuki cross ff neut om oe zorder 2 at f11

    n "oh"

    show natsuki cross ff happ om oe zorder 2 at f11

    n "¿la estas acosando?"

    show natsuki cross ff happ cm oe zorder 2 at t11

    "no creo que esto se considere acoso..."

    show natsuki cross ff lsur cm oe zorder 2 at t11

    mc "porfavor Natsuki, es un problema real"

    show natsuki cross ff lsur om oe zorder 2 at f11

    n "uhm..."

    show natsuki turned ff worr om oe zorder 2 at f11

    n "creo que la vi saliendo del colegio"

    show natsuki turned ff lsur cm oe zorder 2 at t11

    mc "¿¡si!? ¿y dónde podría haber ido?"

    show natsuki turned ff neut om oe zorder 2 at f11

    n "no estoy segura, pero cada vez que nos vamos juntas solemos despedirnos en la casa de ella"

    n "nunca la he visto desviarse, de todos modos vivimos a unas casas"

    show natsuki turned ff neut cm oe zorder 2 at t11

    mc "y crees que haya ido ahi?"

    show natsuki turned ff curi om oe zorder 2 at f11

    n "ni idea"

    show natsuki turned ff curi cm oe zorder 2 at t11

    mc "y podrias llevarme ahi?"

    show natsuki turned lhip rhip ff vsur om ce zorder 2 at f11

    n "asi que ahora tengo que ayudar a un rarito a acosar a mi amiga"

    show natsuki cross ff pout cm oe zorder 2 at t11

    mc "Natsuki esto es en serio, no es por mi es por la seguridad de ella"

    show natsuki cross ff flus cm oe zorder 2 at f11

    n "ya..."

    n "supongo que si es por eso te ayudaré, pero no menciones que fui yo"

    show natsuki cross ff flus cm oe zorder 2 at t11

    "Natsuki me lleva afuera de la escuela"

    #transición a la casa de Yuri
    with dissolve_scene_full
    scene bg street1_morn

    "¿enserio Natsuki estaba buscando monedas por eso? sé que no deberia de meterme pero que tan mal estará"

    "para tener que hacerlo... Podria intentar habl-"

    show natsuki cross ff dist om oe zorder 2 at f11

    n "¿qué sucede con Yuri?"

    show natsuki cross ff neut cm oe zorder 2 at t11

    mc "Hubo una pelea en el club y ella salió rápidamente"

    show natsuki turned ff pout om oe zorder 2 at f11

    n "pelea de... ¿de golpes?"

    show natsuki turned ff pout cm oe zorder 2 at t11

    mc "no fue mas una discusión, disculpa es que me golpeé la cabeza mientras intentaba buscar a Yuri"

    "Natsuki suspiró"

    show natsuki turned ff pout cm oe zorder 2 at f11

    n "oye"

    show natsuki turned ff sad om oe zorder 2 at f11

    n "si Yuri necesita hablar con alguien o la está pasando mal, dile que..."

    show natsuki turned ff angr om oe zorder 2 at f11

    n "la puedo apoyar, somos amigas de todos modos"

    show natsuki turned ff sad cm oe zorder 2 at t11

    mc "si se lo diré"

    with dissolve_scene_full

    scene bg casa_yuri

    "seguí caminando junto a ella, Me pregunto como estará Yuri... ya llevamos caminando un tiempo"

    "el suficiente tiempo para que ell-"

    show natsuki turned ff anno om oe zorder 2 at f11

    n "oye ya llegamos, si te estas arrepitiendo mejor largate a tu casa"

    show natsuki turned ff anno cm oe zorder 2 at t11

    "la pelirosa me sacó de mis pensamientos empujandome"

    mc "muchas gracias Natsuki realmente me ayudaste mucho"

    show natsuki cross angr om ce zorder 2 at f11

    n "si bueno, de nada, espero este bien y tu tambiém"

    show natsuki cross angr om ce zorder 2 at thide
    hide natsuki

    "Natsuki se alejo de mi vista"

    stop music fadeout 1.5

    "me acerqué a la puerta, es una casa muy grande para solo una persona. Espero no esten sus padres"

    "¿cuanto tiempo Yuri llevara lidiando con esto sola...?"

    "presioné el timbre con fuerza"

    "pero nadie vino"

    "lo presioné denuevo"

    mc "¡Yuri! ¿te encuentras en casa?"

    "resonó el sonido de las cortinas al cerrarse desde la segunda planta"

    mc "solo quiero hablar contigo..."

    "por lo menos sé que está aquí"

    "¿pero que puedo hacer?"

    #okay como tal aqui pongo la base pero siento que aqui vendria hiper bien una elección
    #agregar sonido de timbre o de tocar puertya

    "no quiere ayuda..."

    "toque la puerta"

    mc "¡Yuri traje nuestro libro, para que podamos leerlo... quizas en otro lugar como tu casa"

    "los segundo se sienten eternos"

    "luego de mas de un minuto escucho la cerradura abrirse lentamente"

    "aunque la puerta se abria se detuvo abruptamente"

    play music audio.heartbreaking2 fadein 2.0

    y "¿[player]...?"

    y "¿qu-qué haces aqui?"

    mc "como te fuiste temprano del club pensaba en que podriamos ya sabes, leer"

    y "deberías de irte"

    "la puerta se empezo a cerrar lentamente e inmediatamente puse mi pie bloqueandola"

    mc "lo siento Yuri pero no pienso en dejarte sola, quieras o no estaré para ti"

    "sonaba mejor en mi cabeza..."

    "pero no quiero que algún dia no pueda volverla a ver por culpa de esto"

    "la puerta dejó de poner resitencia"

    mc "gracias..."

    scene bg yuri_sala

    "entré dentro de la casa, aunque en la entrada no vi a Yuri"

    "pase a la sala con preocupacion y ahi estaba ella..."

    show yuri turned rcut worr cm oe zorder 2 at t11

    "pusde ver su antebrazo, llenos de cortes aunque alguno aun sigue abiertos... o nuevos"

    mc "Yuri..."

    "esta pobre chica ha estado lidiando con esto todo este tiempo"

    show yuri turned rcut worr om oe zorder 2 at f11

    y "losiento... No queria mostrarte como realmente soy y... que me dejaras de hablar..."

    show yuri turned rcut worr cm oe zorder 2 at t11

    mc "no te dejaré de hablar Yuri"

    show yuri turned rcut lsur om oe zorder 2 at t11

    "saco el libro de mi mochila"

    show yuri turned rcut lsur cm oe zorder 2 at t11

    mc "¿continuamos donde lo dejamos?"

    show yuri turned rcut lsur om oe zorder 2 at f11

    y "okay.."

    show yuri turned rcut lsur cm oe zorder 2 at t11

    "ya no está tratando de evitarme, Yuri dudo unos segundos antes de hablar"

    show yuri turned rcut flus om oe zorder 2 at f11

    y "necesito subir a limpiarme"

    show yuri turned rcut flus cm oe zorder 2 at t11

    mc "claro, tómate tu tiempo"

    show yuri turned rcut flus cm oe zorder 2 at thide
    hide yuri

    stop music fadeout 2.0

    "ella subió las escaleras no sin antes verme, nuestros ojos chocaron otra vez. pero esta vez"

    "no fué como en la escuela, ella está confiando en mi..."

    "tomo asiento en el sofa y abro el libro en la ultima página que leimos"

    "como puedo ayudarla..."

    "me toque la cabeza y senti un dolor punzante, suspire esperando a Yuri"

    #transición y sonido del bzzt

    "*bzzt*"

    "*bzzt*"

    "mi celular empezo a vibrar desde mi bolsillo ¿será Sayori?"

    "atiendo el mensaje"

    #agregar el ??? y el sondio de bzzt para no hacerse wey
    #añadir escena de Yuri con Yuri chiquita

    "???" "deja de evitarme"

    mc "¿qué?"

    "???" "ella no te merece, creeme es una loca"

    mc "quizas te estes confundiendo de numero, soy [player]"

    mc "no recibi respuesta"

    "¿quien ere-"

    y "¿[player]?"

    play music audio.heartbreaking2 fadein 2.0

    "del susto tire mi celular al suelo"

    show yuri turned casual lup rup flus om oe zorder 2 at f11

    y "dis-disculpa no queria asustarte"

    y "¿estabas haciendo algo importante? creo que te vi chateando con alguien"

    show yuri turned casual lup rup flus cm oe zorder 2 at t11

    "noto que mi celular esta tirado en el suelo, me asustó mas el mensaje que Yuri"

    mc "No, es solo que me tomaste de sorpresa"

    "recogí mi celular del suelo, el número desconocido estaba escribiendo, más sin embargo guardé mi celular"

    "anque aun me pregunto quien será, realmente me importa mas Yuri en estos momentos"

    mc "de hecho te estaba esperando"

    show yuri turned casual rup lsur cm oe zorder 2 at t11

    "Todo ha estado pasando muy rapido"

    "todo ha sido demasiado rápido y aunque quiero ayudar me siento cansado"

    #añadir el efecto de panico aunque me critiquen 

    show yuri turned casual rup worr om oe zorder 2 at f11

    y "pe-perdona te hice esperar mucho timepo"

    show yuri turned casual rup worr cm oe zorder 2 at t11

    "Yuri se sentó a mi lado, la miré unos segundo a los ojos"

    "saqué el libro"

    mc "deberiamos de continuar ¿no?"

    #añadir la historia aunque me critiquen

    #porcierto dependiendo de la historia este dialogo cambiará debido a que todavia no hay una historia definida, aunque me critiquen

    "despues de leer esa linea deje de concentrarme en la historia, miré a Yuri. Pero ella no hizo lo mismo"

    "\"el Chico de la historia me recuerda a ti. Yuri\""

    #si no me hago wey añado el efecto de recuerdos, aunque me critiquen

    "Yuri... sus ojos violetas estan llorando"

    show yuri turned casual sad om oe zorder 2 at f11

    y "¿sabes porque elegí este libro para que podamos leerlo [player]?"

    show yuri turned casual sad cm oe zorder 2 at t11

    "..."

    show yuri turned casual flus om oe zorder 2 at f11

    y "porque no se como hablar con los demás"

    y "no sé como describir mis sentimientos"

    y "mis problemas... Solo sé leer libros"

    y "creí que al compartir este libro podria mostrarte un vistazo de como soy en realidad"

    show yuri turned casual cry om ce zorder 2 at f11

    y "pero... fué un terrible error porque ahora"

    show yuri turned casual cry om oe zorder 2 at f11

    y "ves como realmente soy..."

    show yuri turned casual cry cm oe zorder 2 at t11

    mc "yo..."

    show yuri turned casual rup cry cm oe zorder 2 at t11

    "las palabras no salieron de mi, intento acercarme a Yuri pero ella retrocedió"

    show yuri turned casual rup cry om ce zorder 2 at f11

    y "sé porque estas aqui"

    show yuri turned casual rup cry om oe zorder 2 at f11

    y "no querías leer... tu viniste porq- porque..."

    show yuri turned casual rup cry cm oe zorder 2 at t11

    "Yuri no pudo continuar hablando"

    show yuri turned casual neut me e1g b1b zorder 2 at t11

    "¿por qué vine aqui?"

    "recientemente conocí a Yuri, pero es alguien importante para mi"

    mc "es cierto, no vine aqui para continuar leyendo"

    "levanto la mirada hacia mis ojos, yo tambien hacia los suyos"

    mc "no vine porque sentía pena por ti"

    mc "vine porque..."

    mc "quisiera ayudar, pero ayudarte a ti, Yuri"

    mc "lo que haces es peligroso"

    mc "un dia podrías equivocarte y... no podria volverte a ver"

    show yuri turned casual cry cm ce zorder 2 at f11

    y "[player]..."

    show yuri turned casual neut mi e1g b1b zorder 2 at f11

    y "no puedo parar"

    y " ya lo he intentado varias veces"

    show yuri turned casual rup neut mi e1g b1b zorder 2 at f11

    y " se lo que me podria pasar si me llegara a equivocar por un centimetros mas sin embargo"

    y "no"

    y "puedo"

    y "ᵈᵉʲᵃʳ ᵈᵉ ʰᵃᶜᵉʳˡᵒ"

    show yuri turned casual rup neut md e1g b1b zorder 2 at t11

    "regresé a acercarme a Yuri pero en lugar de retroceder ella se quedó quiera"

    "suavemente agarré su mano con la mia. sostuve su palida y fria mano"

    mc "pero esta vez no estas sola"

    mc "prometo ayudarte en todo lo posible, para que juntos puedas superar esto"

    mc "tu y yo"

    show yuri turned casual rup cry om oe zorder 2 at f11

    y "pero... yo solo te he arrastrado hasta aqui"

    y "estuviste en el momento en cuando le dije a Monika... ES-estabas ahi y aun asi decidiste en seguir"

    show yuri turned casual rup cry cm oe zorder 2 at t11

    "porque te amo Yuri"

    mc "porque es lo que deberia de hacer Yuri, ayudarte sin importar la circunstacia"

    "te amo"

    "pero"

    "no sé que es amar..."

    show yuri turned casual rup cry om oe zorder 2 at f11

    y "[player]... yo nunca he tenido amigos"

    show yuri casual rup cry cm oe zorder 2 at t11

    mc "eso no es cierto"
  
    mc "me tienes a mi. Prometo hacer todo lo posible con tal que nada ni nadie te lastime"

    show yuri turned casual rup sad cm ce zorder 2 at t11

    y "..."

    show yuri turned casual sad cm oe zorder 2 at t11

    "quizás este sea un momento indicado"

    "agarré mi mochila y de ella sacque una hoja de papel"

    mc "sé que no estamos en el club, pero"

    mc "escribí esto... para ti"

    show yuri turned casual lup rup worr om oe zorder 2 at f11

    y "¿para mi?"

    show yuri turned casual lup rup worr cm oe zorder 2 at t11

    mc "¿recuerdas que me dijiste? acerca de plasmar mis pensamientos, lo hice expresando"

    mc "lo que siento por ti"

    show yuri turned casual lup rup sad om oe zorder 2 at f11

    y "pe-pero, no escribí nada"

    show yuri turned casual lup rup sad cm oe zorder 2 at t11

    mc "esta bien ¿te gustaría leerlo?"

    "estiro mi mano para darle el poema a Yuri"

    "ella asiente y sostiene la carta"

    #aqui se agrega el poema 

    show yuri turned casual lup cry cm ce zorder 2 at t11

    "derrepente, ella empieza a lagrimear. Sus mejillas quedan mojadas por las gotas de sus ojos"

    show yuri turned casual lup cry cm oe zorder 2 at t11

    mc "Yuri, realmente quisiera apoyarte"

    mc "Ayer vi como Monika te dijo algo en voz baja y como me evitaste"

    show yuri turned casual lup cry om oe zorder 2 at f11

    y "y-yo..."

    show yuri turned casual lup cry cm oe zorder 2 at t11

    "La voz de Yuri se quebró, su manga se volvió rojiza. Ella no habia limpiado sus brazos..."

    "Yuri se levantó, antes que siguiera la agarré de la mano"

    show yuri turned casual lup cry om oe zorder 2 at f11

    y "[player] por favor..."

    show yuri turned casual lup cry cm ce zorder 2 at f11

    mc "confia en mi"

    show yuri turned casual lup cry cm oe zorder 2 at r11


    #añadir Yuri con cortes casual


    "aunque no muy segura, me dio suavemente su mano. la manga de su mano bajo sola"

    "Yuri..."

    "Yuri tiene varios cortes... nuevos, viejos... ligeros y... profundos"

    "Cicatrices sobre cicatrices"

    "no puedo quedarme quiero observando"

    mc "¿tienes un botiquin o curas?"

    y "creo que si..."
    stop music fadeout 2.0
    with dissolve_scene_full
    scene bg bedroom
    play sound closet_open

    "10:43 AM"

    "Este sábado es lo que más necesito luego de una semana tan complicada"

    "Yuri, pudo confiar en mi e incluso me pudo dar su número"

    "pero aun me inquieta todo lo demás..."

    "Sayori llorando en el club y yo siendo su mejor amigo no pude apoyarla..."

    "Natsuki también parece tener un problema que aún no puedo saber"

    "desde ayer he estado recibiendo mensajes de un numero extraño"

    "se me está complicando seguir el ritmo a todo... Siento que en algún momento solo caeré en el suelo"

    "pero Yuri"

    "luego de curar su heridas quedamos en que ibamos a salir a salir hoy"

    "aunque estuve nervioso luego de irme de su casa, yo confio en Yuri"

    "es un dia hermoso hayá afuera"

    #cambio de escena a la cocina
    with wipeleft_scene 
    scene kitchen

    "saqué mi telefono para escribirle a Yuri, desde que me fuí de su casa no hemos hablado mucho."

    mc "Hola Yuri, estoy saliendo de mi casa pero antes de ir quería saber como estás"

    "Sé que hoy será un día bueno para ambos"

    "*bzzt*"

    y "Ya me encuentro lista, gracias por preguntar."

    #cambio de escena suave
    with wipeleft_scene 
    scene house

    "me acerqué a la puerta de la casa"

    "toque el timbre"

    pause 0.5
    #agregar sonido de timbre

    "escuché como la puerta se abrió"

    #agregar ropa de Yuri

    show yuri 1cb zorder 2 at f11

    play music audio.t6 fadein 2.0

    y "hola [player]"

    show yuri 1ca zorder 2 at t11
    
    mc "pensaba que me ibas a dejar plantando"

    show yuri 1co zorder 2 at f11

    y "u-uh no claro que no haria eso"

    show yuri 1ca zorder 2 at t11

    mc "no lo digo enserio... Entonces... me acompañas?"

    show yuri 1cd zorder 2 at f11

    y "¡si! porsupuesto"

   

    #escena de transición 
    show yuri 1cd zorder 2 at thide
    hide yuri
    with wipeleft_scene 
    scene bg ciudad_calle_nublado

    show yuri 1cu zorder 2 at t11

    "Estuvimos caminando juntos por la calle"

    "aunque Yuri seguia mi paso lentamente"

    "hay muchas plazas en la ciudad"

    "restaurantes, tiendas, centros comerciales ¿a donde le gustará ir a Yuri?"

    "mientras seguimos recoriendo la ciudad noto una cafeteria, a ella le gusta el té supongo que es buena idea"

    show yuri 1ce zorder 2 at t11

    mc "¿te gustaría ir a esa cafeteria?"

    show yuri 1cd zorder 2 at f11

    y "me parece bien, en realidad suelo visitar este lugar frecuentemente"

    scene bg cafe

    show yuri 1ce zorder 2 at t11

    "mientras estabamos en el menú me puse a analizar el menú"

    mc "ya que sueles ir aqui ¿alguna recomendación?"

    show yuri 1cf zorder 2 at t11

    y "uh, hay demasiadas cosas para probar, no quisiera elegir algo que no te giuste"

    show yuri 1cf zorder 2 at t11

    mc "tranquila, no soy tan exigente"

    show yuri 1cb zorder 2 at f11

    y "supongo que... podrías beber un té blanco"

    show yuri 1ca zorder 2 at t11

    mc "me parece bien y que escogerás?"

    show yuri 1cb zorder 2 at f11

    y "un té Oolong"

    show yuri 1cc zorder 2 at t11

    mc "oh creo que ese fué el bebimos mientras estavamos en el club"

    show yuri 1cd zorder 2 at f11

    y "si es ese mismo"

    show yuri 1ca zorder 2 at t11

    "si, el club"

    "¡Sayori! despues de terminar esta cit... salida iré a ver como está ella"

    "me he olvidado completamente de ella... del como ha estado"

    show yuri 1cv zorder 2 at f11

    y "(hola me da un té Oolong)"

    y "(¿hola me podria dar un té Oolong?)"

    y "(¿podría pedir un té Oolong?)"

    show yuri 1co zorder 2 at t11

    "me volteé hacia Yuri"

    mc "¿me estabas diciendo algo?"

    show yuri 1cq zorder 2 at f11

    y "estaba practicando lo que iba pedir"

    y "¿no te sueles preparar mentalmente para pedir algo?"

    show yuri 1cu zorder 2 at t11

    mc "¿qué?"

    show yuri 1cq zorder 2 at f11

    y "oh si... que verguenza... Yo suelo hacerlo seguido"

    show yuri 1cw zorder 2 at t11

    "mierda, como podría recuperar la situación"

    ##################
    show yuri 1cs zorder 2 at t11
    mc "no suelo hacero pero siento que todos nos preparamos para algo en cierta medida"



    #aqui una elección. mas arriba quizas 

    show yuri 1cn zorder 2 at t11

    mc "ademas es lindo"

    show yuri 1cn zorder 2 at f11

    y "¡que!"

    stop music fadeout 2.0

    show yuri 1ce zorder 2 at t11
    
    "vendedor" "siguiente"

    "vendedor" "buenos días ¿qué les gustaría ordenar?"

    mc "un té blanco para mi porfavor"

    "vendedor" "anotado ¿y usted señorita?"

    show yuri 1co zorder 2 at f11

    y "uhhh... u-un"

    y "u-un... t-... té OO-"

    show yuri 1cn zorder 2 at t11

    "cliente" "¿oigan podrían apurarse? tengo un tiempo limitado"

    "vendedor" "señorita, un té ¿de?"

    "el vendedor deja de mirar a Yuri y voltea a ver a la fila de atrás"

    "vendedor" "podría apurarse ¿porfavor?"

    #aqui eleccion de si pedir por yuri o deja que Yuri elija, la hisotira como tal seguira aqui por una manera de la ruta buena

    show yuri 1ck zorder 2 at t11
    mc "a ella le gustaría un té Oolong"

    "vendedor" "té Oolong y blanco ¿sería todo?"
    show yuri 1ck zorder 2 at thide
    hide yuri

    mc "si, gracias"

    "pagué la orden y junto a Yuri nos sentamos a una mesa vacia, cerca de las ventanas del lugar"

    show yuri 1cv zorder 2 at f11

    y "l-lo hice terrible... y seguramente te hice pasar pena, losiento"

    show yuri 1cu zorder 2 at t11

    mc "no hay de que disculparse Yuri"

    show yuri 1cw zorder 2 at f11

    y "pe-pero ese señor nos grito..."

    show yuri 1cv zorder 2 at f11

    y "te avergonzé ¿verdad?"

    show yuri 1cv zorder 2 at t11

    mc "Yuri, si quieres saber mi respuesta deja de voltear la mirada"

    show yuri 1cs zorder 2 at t11

    mc "Yuri está bien, no estoy avergonzado ni nada parecido y sobretodo"

    mc "a quien le importa las personas que gritan por cualquier minima cosa"

    mc "no te preocupes por lo que digan los demás"

    show yuri 1ct zorder 2 at f11

    y "me preocupo por lo que digas tu..."

    show yuri 1cs zorder 2 at t11


    mc "entonces todoe está bien, en realidad yo deberia de pedir perdón"

    mc "te distraje mientras te preparabas para pedir"

    show yuri 1cf zorder 2 at f11

    y "gracias, por ordenar por mi, enserio lo aprecio"

    show yuri 1ca zorder 2 at t11

    mc "no hay problema"

    "*bzzt*"

    "el camarero pone las ordenes en la mesa"

    "*bzzt*"

    mc "y ¿ya ha-"

    "*bzzt*"

    show yuri 1cb zorder 2 at f11

    y "puedes contestar, no me molesta"

    show yuri 1ca zorder 2 at t11

    mc "no, solo lo apagaré un rato, dame un momento"

    "agarré mi celular y vi los mensajes del numero desconocido"

    "???" "¿ya responderás estas ocupado \"bebiendo té\"?"

    mc "jodete"

    "apagué mi celular"

    show yuri 1ce zorder 2 at t11

    mc "sabes, me gustaba pasar tiempo en el club contigo"

    show yuri 1cd zorder 2 at f11

    y "a mi tambien, era agradable... eres"

    show yuri 1ca zorder 2 at t11

    mc "honestamente, me uní al club por los cupcakes y Sayori"

    show yuri 1cj zorder 2 at f11

    y "siendo sincera, cuando me uní al club pensé que podria encontrar amigos con gustos similares a los mios"

    show yuri 1ct zorder 2 at f11

    y "como la pasión que tengo por lo libros, siempre me he sentido un poco aislada de los demas"

    y "tenia la esperanza de poder deja de ser tan indiferente..."

    y "parece que no salió como me esperaba"

    show yuri 1cw zorder 2 at f11

    y "Monika"

    y "ella me invitó al club primeramente"

    show yuri 1cv zorder 2 at f11

    y "no quisiera que la odies... por mi culpa"

    y "sé que es una buena persona..."

    show yuri 1cu zorder 2 at t11

    "¿una buena persona?"

    "una buen persona no diría que te suicides"

    "pero, una buena persona tampoco diria que va a matar a alguien..."

    show yuri 1cu zorder 2 at t11

    mc "prefiero de no hablar de ella pero"

    show yuri 1cs zorder 2 at t11

    mc "estas equivocada en lo de socializar, me refiero. Estas aquí conmigo"

    mc "tienes a Natsuki que si excluyes las diferencias estoy seguro que serian buenas amigas"

    mc "también a Sayori quien estoy seguro te considera su amiga"

    mc "me encanta estar contigo hoy, pero odio que la razon por la que estemos aqui sea Monika"

    show yuri 1ct zorder 2 at f11

    y "tienes razón, denuevo"

    show yuri 1cb zorder 2 at t11

    "Yuri me sonrie, dejando su pena atrás"

    "tomé un sorbo de mi taza de té"

    show yuri 1cd zorder 2 at t11

    mc "Elegiste bien Yuri"

    show yuri 1ce zorder 2 at t11

    mc "Oye Yuri, ahora que lo pienso ¿te gustaría acompalarme a la casa de Sayori?"

    show yuri 1cf zorder 2 at f11

    y "no tengo problema pero suenas preocupado por algo"

    show yuri 1ct zorder 2 at t11

    mc "Ella se veía muy decaida el dia que nos fuimos temprano del club"

    mc "y queria pasar por lo menos a saludarla y que no se sienta sola en esto"

    show yuri 1cw zorder 2 at f11

    y "por estar discutiendo no me dí cuenta de como los demas la estaban pasando a mi alrededor..."

    show yuri 1ct zorder 2 at f11

    y "personas que la estan pasando peor que yo..."

    show yuri 1cq zorder 2 at f11

    y "me gustaria acompañarte y espero poder hablar con Sayori acerca de..."
    
    y "de lo que paso"

    show yuri 1ca zorder 2 at t11

    mc "estoy seguro que ella se pondrá super feliz de vernos a ambos"

    "luego de finalizar nuestras bebidas salimos de la cafeteria para dirigirnos a la casa de Sayori"

    with wipeleft_scene 
    scene residential

    show yuri 1cu zorder 2 at t11

    "llegamos a la casa de Sayori y toqué la puerta"

    "..."

    "sin respuesta"

    "..."

    show yuri 1ct zorder 2 at f11

    y "quizás ella no este en casa"

    show yuri 1cn zorder 2 at t11

    "abri la puerta de la casa"

    show yuri 1cn zorder 2 at f11

    y "¿oy-oye estas seguro de hacer eso?"

    show yuri 1cn zorder 2 at t11

    mc "¿porqué no?"

    mc "Ella solia hacer lo mismo cuando no queria salir a jugar"

    show yuri 1cb zorder 2 at f11

    y "Recuerdo que Sayori nos solia hablar de anecdotas parecidas"

    show yuri 1ca zorder 2 at t11

    "brrr"

    "brrr"

    show yuri 1ci zorder 2 at f11

    y "disculpa [player] ¿puedes adelantarte? atenderé la llamada"

    mc "está bien, de todos modos veré si está Sayori"

    show yuri 1ci zorder 2 at thide
    hide yuri
    
    with dissolve_scene_full
    scene black 

    mc "¿Sayori?"

    "es extraño el silencio o no tener una bienvenida de Sayori"

    "quizás si le haya afectado el ánimo lo que ocurrió..."

    "Subí las escaleras y me dirigí a su puerta"

    "..."

    mc "¿Sayori puedo entrar?"

    "..."

    mc "oye, enserio quiero hablar contigo asi que espero no estes dorm-"

    show sayori turned casual rup flus om oe zorder 2 at f11

    scene bg sayori_bedroom

    s "¿¡[player]!?"


    s "Qué... ¿qué haces aquí?"

    show sayori turned casual rup flus cm oe zorder 2 at t11

    mc "bueno queria visitarte y no vengo solo, tambien Yuri"

    show sayori turned casual dist om oe zorder 2 at f11

    s "oh Yuri.. que bueno"

    show sayori turned casual dist cm oe zorder 2 at t11

    "Si definitivamente Sayori está desanimada"

    "me quedé parado en el tomo de la puerta, en un silencio incomodo"

    show sayori turned casual laug om oe zorder 2 at f11

    s "así que ¿tu y Yuri no?"

    show sayori turned casual happ cm oe zorder 2 at t11

    mc "N-no lo malpienses, solo estamos aqui como amigos"

    show sayori turned casual neut om oe zorder 2 at f11

    s "es dificl ocultar los sentimientos, sobretodo cuando los ves todos los dias"

    s "desde el primer dia note esa conexión entre ustedes"

    show sayori turned neut n2 md e1b b1b zorder 2 at t11

    "Esto... no suena como lo diria Sayori parece más... ¿honesto?"

    mc "sea lo que sea que intentes decir, estoy seguro que estas equivocada"

    show sayori turned sad om oe zorder 2 at f11

    s "me alegra que sean amigos... Y-yo... Estoy feliz por eso"

    show sayori turned sad cm ce zorder 2 at t11

    mc "¿Sayori?"

    play music audio.t10

    show sayori turned neut n1 mj e1g b1c zorder 2 at t11

    "Ella tiene los ojos lagrimosos, no se que esta pasando"

    mc "¿Sayori sucede algo?"

    "entré a su cuarto"

    mc "sé que esta pasando algo"

    mc "como mencionas es dificil ocultar sentimientos y más si te conozco desde la infancia"

    show sayori turned neut n1 mb e1g b1c zorder 2 at t11

    "Sayori se limpió los ojos"

    show sayori turned neut n1 mb e4d b1c zorder 2 at f11

    s "jejeje..."

    show sayori turned neut n2 mg e1g b1c zorder 2 at f11

    s "estas equivocado [player]"

    s "siempre he sido así pero, por primera vez no puedo ocultarlo"

    show sayori turned neut n2 me e1g b1c zorder 2 at t11

    mc "¿ocultar que Sayori?"

    show sayori turned worr om oe zorder 2 at f22

    s "ocultar... N-no... creo que deberias de irte, no debes de verme asi..."

    show sayori turned worr cm oe zorder 2 at t22

    "Sayori..."

    "siento la misma sensación de cuando vi a Yuri cortandose... Puedo ver en Sayori esa misma expresion"

    mc "Sayori si hay algún problema que haya ocurrido, solo dime si es por lo del clu-"

    show sayori turned sad om oe zorder 2 at f11

    s "no creo que lo entiendas [player]. Yo no quiero ser ayudada"

    show sayori turned sad cm oe zorder 2 at t11

    "\"no quiero tu ayuda\""

    show sayori turned sad om ce zorder 2 at f11

    s "La ayuda solo es para quienes se lo merecen"

    show sayori turned sad cm oe zorder 2 at t11

    "Mi mente no esta soportando las palabras de Sayori"

    mc "Sayori se honesta conmigo porfavor ¿qué sucede?"

    show sayori turned sad om ce zorder 2 at f11

    s "jeh... ¿enserio quieres que lo tire verdad?"

    s "[player]..."

    show sayori turned laug cm ce zorder 2 at f11

    s "he pasado toda mi vida lidiando con la depresión"

    s "siempre he tenido esos pensamiento en mi mente, que no deberia de ser feliz, que no deberia de continuar"

    show sayori turned cry om oe zorder 2 at f11

    s "¿sabes porque salgo tarde mi escuela?"

    s "porque todos los días no encuentro una razón para levantarme de la cama y caminar"

    s "todos los días no encuentro una razón para comer, para continuar"

    s "cuando llego al instituto solo pienso en irme"

    show sayori turned cry om ce zorder 2 at f11

    s "¿porqué cuando despierto no puedo ver el sol? solo unas nubes nubladas"

    show sayori turned cry om oe zorder 2 at f11

    s "¿porqué cuando salgo de mi casa empieza a llover?"

    s "dime porque todos los días tengo que fingir una personalidad que no soy con tal de no afectar a los demás"

    s "¿porqué hacer amigos cuando todos ellos somo me usan para poderse sentir mejor consigo mismo?"

    show sayori turned cry cm ce zorder 2 at f11

    s "cuando siempre eres visto como \"el tonto\""

    s "la chica que siempre está forzando una sonrisa"

    show sayori turned cry om oe zorder 2 at f11

    s "porque abrir los ojos todas las mañanas"

    s "cuándo la unica persona y razón por la cual intento aguantar todo este dolor y continuar"

    show sayori turned neut om oe zorder 2 at f11

    s "Está enamorado de otra chica..."

    show sayori turned neut cm oe zorder 2 at t11

    "siento como si mi mundo se estuviera destruyendo por cada palabra de Sayori"

    "he estado ignorando... a la chica que siempre me ha intentado ayudar..."

    show sayori turned neut cm oe zorder 2 at thide
    hide sayori 

    scene black

    s "¿e-eh?"

    "abracé a Sayori, realmente no pude aguantar las lagrimas del momento"

    mc "perdoname..."

    mc "siento no haber estado contigo todo este tiempo..."

    mc "siento no haberme dado cuenta de esto..."

    mc "te prometo que ha partir de hoy haré todo lo posible para que te sientas me-"

    s "[player]"

    "Sayori, no me devolvió el abrazo"

    "ella puso sus manos en mi pecho, para alejarme"

    s "no lo entiendes"

    scene bg sayori_bedroom
    show sayori turned casual lup rup cry cm oe zorder 2 at f11

    s "nadie puede entenderlo"

    s "no quiero que tu... que alguien se preocupe por mi"

    s "es agridulce de conocer... ¿cierto?"

    show sayori turned casual lup rup neut n1 ma e1h b2c zorder 2 at t11

    "Mi corazón esta latiendo muy fuerte y... Quiero ayudarla pero mi mente no copera..."

    show sayori turned casual lup rup neut n1 mc e1h b2c zorder 2 at f11

    s "aveces logro sentirme bien pero inmediatamente siento como si la culpa me estuviera aplastando sin cesar"

    s "ya entendí porque realmente viniste"

    show sayori turned casual lup rup neut n1 mc e4e b2c zorder 2 at f11

    s "es el universo castigandome, se que lo merezco... pero es tan horrible... tener este sentimiento"

    s "verte aquí con Yuri..."

    show sayori turned casual lup rup neut n1 mc e1h b2b zorder 2 at f11

    s "es como si me intentaras mantener viva mientras me incruzstas una lanza en el pecho"

    s "y tu [player]..."

    s "eres todo para mi, eres mi mundo. Cada vez que caminamos, cada vez que hablamos..."

    s "me hace querer llorar por todo el dolor que siento"

    show sayori turned casual lup rup neut n1 mc e4e b2c zorder 2 at t11

    mc "Sayori..."

    show sayori turned casual lup rup neut n1 mc e1h b2c zorder 2 at t11

    "quite sus manos de mi pecho y puse las mias en sus hombros"

    mc "para mi es dificil poder entenderte y sé que he sido un estupido todos estos años..."

    mc "pero yo haré todo por ti Sayori, estaré siempre a tu lado..."

    show sayori turned casual lup rup neut n1 mh e1h b2c zorder 2 at f11

    s "pero [player]..."

    show sayori turned casual lup rup neut n1 mj e1h b2c zorder 2 at f11

    mc "Sayori"

    #mrd no quiero continuar esta parte :(

    menu Sayori_eleccion:
        "siempre serás mi mejor amiga.":
            "\"tu siempre serás mi mejor amiga\""
            jump siempre_serás_mi_mejor_amiga
        "Te quiero Sayori.":
            mc "Sayori... yo honestamente te quiero en mi vida"
            jump te_quiero_sayori

    label siempre_serás_mi_mejor_amiga:
        show sayori turned casual lup rup cry om ce zorder 2 at f11
        s "vete..."

        show sayori turned casual lup rup cry om ce zorder 2 at t11

        mc "pero Sayori"

        show sayori turned casual lup rup cry om oe zorder 2 at f11

        s "¡Vete de mi casa porfavor!"

        show sayori turned casual lup rup cry cm oe zorder 2 at t11

        "intenté volverme a acercar a Sayori y ella tiró un espejo cerca de mi"

        show sayori turned casual lup rup cry om oe zorder 2 at f11

        s "¡largate ahora mismo!"

        show sayori turned casual lup rup cry cm ce zorder 2 at r11

        mc "..."

        "me fuí de la habitación"
        show sayori turned casual lup rup cry cm ce zorder 2 at thide
        hide sayori
        with dissolve_scene_full


        jump yuri_continuación

    label te_quiero_sayori:
        with dissolve_scene_full
        scene black
        s "mc..."
        s "tu eres la única razón por la cual yo continuo viviendo todos los días"

        mc "tranquila Sayori... Siento que a su vez deberias de ir a un psicologo"
        mc "te acompañaré en cada terapia Sayori"

        s "[player]"
        s "gracias por estar aqui"
        s "no se que hubiera pasado en unos dias..."

        "abracé denuevo a Sayori"
        "y ella me devolvió el abrazo"
        with dissolve_scene_full



        jump yuri_continuación

    label yuri_continuación:
        stop music fadeout 1.5
        scene residential
        play music audio.t6 fadein 1.5
        "salí de la casa de Sayori y cerré la puerta de su casa"

        "Yuri aún seguia en la llamada pero luego de unos segundo colgó"

        show yuri 1ct zorder 2 at f11

        y "y ¿se encuentra Sayori?"

        show yuri 1ci zorder 2 at t11

        "como quisiera poderte mentirle en estos momentos..."

        mc "si se encuentra en su habitación"

        show yuri 1cj zorder 2 at f11

        y "entonces ¿porqué cerraste la puerta de la casa? te miras agitado.."

        show yuri 1co zorder 2 at t11

        mc "Sayori no quiere hablar en estos momentos"

        show yuri 1cn zorder 2 at f11

        y "¿porqué?"

        show yuri 1ck zorder 2 at t11

        "suspiré"

        mc "es largo de explicar, pero Sayor-"

        #añadir sonido de cerradura, de cuando se cierra una puerta

        mc "será mejo irnos Yuri..."

        show yuri 1ce zorder 2 at f11

        y "está bien [player]"

        y "quizás solo necesite un tiempo para poder acomodar sus pensamientos, espero lo mejor para ella"

        show yuri 1ca zorder 2 at t11

        mc "si..."

        "Sayori mi mejor amiga se confeso conmigo... todos sus sentimientos, lo que llevaba cargando todo este tiempo"

        "nunca pude llegar a pensar en que ella sufriria depresión"

        show yuri 1cg zorder 2 at t11

        "siempre le hecho bromas o burlado de ella por llegar tarde, estar despeinada... llevar el uniforme mal..."

        "que depresión tan fuerte tendrá ella... para costarle levantarse de la cama"

        "todo ha sido mi culpa..."

        show yuri 1cg zorder 2 at f11

        y "¿[player]?"

        show yuri 1cg zorder 2 at t11

        mc "perdoname... me perdí en mis pensamientos"

        show yuri 1ch zorder 2 at f11

        y "hmm... comunmente cuando me pasa eso suelo ir a la biblioteca, me ayuda a despejar la mente"

        show yuri 1ck zorder 2 at t11

        mc "quizás un buen libro me ayude"

        mc "entonces ¿vamos?"

        show yuri 1cb zorder 2 at f11

        y "porsupuesto"

        show yuri 1cb zorder 2 at thide
        hide Yuri
        with dissolve_scene_full


        #poner la scene biblioteca
        scene bg library_aft

        show yuri 1cb zorder 2 at f11

        y "oye [player] mira es Guia del Sakura, la continuación de insolación infinita"

        show yuri 1ca zorder 2 at t11

        mc "¿guia del sakura? no suena como la continuación del libro que leemos"

        mc "¿porqué Sakura?"

        show yuri 1ch zorder 2 at f11

        y "la chica se colgó en un arbol de Sakura"

        show yuri 1ck zorder 2 at f11

        mc "si... cierto"

        show yuri 1cm zorder 2 at t11


        #aqui podemos hacer una especie de referencia a Sayori y que eso haga que Sayori lo recuerde

        mc "compralo, asi cuando terminemos el libro empezamos a leer el nuevo"

        show yuri 1cq zorder 2 at f11

        y "sobre eso, todavia no ha salido, solo es como una muestra de excivision"

        show yuri 1ce zorder 2 at t11

        mc "oh que curioso, ir soltando pequeños adelantos de una historia para ir emocionando al publico y recibir apoyo"

        mc "*cof cof*"

        show yuri 1ce zorder 2 at thide
        hide yuri

        "estuve acompañando a Yuri por la biblioteca buscando un libro ideal"

        #aqui quizas podriamos alargar un poco la escena agregando como que se encuentran x libro pero dsp

        "despues de leer con Yuri fuimos a dejar el libro en su lugar antes de retirarnos"

        "vendedor" "ey Yuri ¿cómo estas?"

        show yuri 1cq zorder 2 at t11

        "e inmediatamente Yuri salio de la biblioteca, mire al vendedor y me quedé confundido"

        show yuri 1cq zorder 2 at thide
        hide yuri

        #aqui poner scene ciudad
        with wipeleft_scene 
        scene bg ciudad_calle_nublado
        show yuri 1cq zorder 2 at t11

        mc "¿oye ese tipo te hizo algo?"

        show yuri 1cv zorder 2 at f11

        y "n-no es eso"

        show yuri 1cu zorder 2 at t11

        mc "¿lo conoces?"

        show yuri 1cq zorder 2 at f11

        y "y-yo..."

        show yuri 1cq zorder 2 at t11

        "creo que estoy poniendo mas nerviosa a Yuri en lugar de ayudar"

        show yuri 1cu zorder 2 at t11

        mc "está bien, tomate el tiempo que necesites"

        pause 5.0

        show yuri 1ct zorder 2 at f11

        y "el suele intentar entanblar conversaciones conmigo"

        show yuri 1ct zorder 2 at t11

        mc "pero no te ha hecho nada malo ¿cierto?"

        show yuri 1cw zorder 2 at f11

        y "n-no... solo intento evitarlo cada vez que vengo aqui, incluso cuando está atendiendo espero a que acabe su turno"

        show yuri 1cq zorder 2 at t11

        mc "bueno quizas puedas decirle que no quieres hablar"

        show yuri 1cq zorder 2 at f11

        y "decir..."

        show yuri 1cq zorder 2 at t11

        "esto es un poco... surealista, estar con ella tanto tiempo no me ha permitido ver lo reservada que es"

        #ahora casa de Yuri
        stop music fadeout 2.0
        with dissolve_scene_full
        scene bg casa_yuri
        play music audio.heartbreaking2 fadein 2.0
        show yuri 1cd zorder 2 at t11

        mc "hoy fué un dia increible Yuri quizas podríamos salir en otro momento"

        mc "hasta luego cui-"

        show yuri 1cq zorder 2 at f11
        
        y "o-oye [player]"

        y "¿no te gustaría entrar a mi casa y leer un rato"

        show yuri 1cq zorder 2 at t11

        mc "..."

        show yuri 1cq zorder 2 at f11

        y "olvidalo has-"

        show yuri 1cn zorder 2 at f11

        mc "porsupuesto Yuri el gusto es mio"

        show yuri 1cn zorder 2 at thide
        hide yuri 


        #casa de Yuri
        with wipeleft_scene 
        scene bg yuri_sala

        "ahora que lo recuerdo no traje mi mochila, donde tengo el libro"

        mc "oye Yuri se me olvidó traer el libro"

        show yuri 1cb zorder 2 at f11

        y "yo tengo una copia en la repisa"

        show yuri 1ca zorder 2 at t11

        mc "ah, cierto lo habia olvidado"

        #añadir ps casa de Yuri de noche
        with dissolve_scene_full
        scene bg yuri_sala_noche

        show yuri 1cm zorder 2 at t11

        "estuvimos leyendo una gran parte de la tarde, creo que Yuri está dormida"

        mc "yuri despierta"

        "la movi un poco y lentamente ella abrio los ojos"

        show yuri 1co zorder 2 at f11

        y "a-ah disculpa, me quedé completamente dormida ¿qué hora es?"

        show yuri 1cs zorder 2 at t11

        "revise mi celular"

        "sin carga"

        show yuri 1cg zorder 2 at f11

        y "21:59 es muy tarde para que regreses solo"

        show yuri 1co zorder 2 at t11

        mc "tampoco quisiera ser un intruso en tu casa ¿sabes?"

        show yuri 1cb zorder 2 at f11

        y "para mi está bien que te quedes"

        show yuri 1ca zorder 2 at t11

        mc "¿enserio? ¿y dónde dormiria?"

        show yuri 1ch zorder 2 at f11

        y "(no puedo dejar que duermas en la sala el es mi invitado...)"

        show yuri 1ch zorder 2 at t11

        "espera ¿Enserio pasará en lo que estoy pensando?"

        show yuri 1ch zorder 2 at f11

        y "sé que sonara un podo ridiculo pero..."

        show yuri 1ch zorder 2 at t11
        
        "Yuri enserio me pedirá... ¿que duerma con ella?"

        show yuri 1cq zorder 2 at f11

        y "mi cama es bastante grande y cómoda..."

        show yuri 1cq zorder 2 at t11

        "mi boca no responde"

        show yuri 1cv zorder 2 at f11

        y "disculpa, dormiré aqui y tu en mi cuarto..."

        show yuri 1ca zorder 2 at t11

        mc "n-no de hecho no veo algún problema en que durmamos ambos"

        show yuri 1cc zorder 2 at f11
    
        y "gracias [player]"

        y "por ti mi dia ha sido increible"

        show yuri 1ca zorder 2 at t11

        mc "gracias Yuri opino lo mismo de hoy"

        "Yuri me llevó a su cuarto"
        stop music fadeout 1.5
         

    
        with dissolve_scene_full






























    




    







    



    return

