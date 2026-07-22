
label Act_1:

    jump .memories_mc

label .memories_mc:
    stop music fadeout 0.2
    # Sonido despertador
    play music clock 
    "..."
    "..."
    "..."
    stop music fadeout 0.5
    scene bg bedroom
    with fade
    "Me levanto, apago el despertador, miro a mi alrededor buscando consuelo."
    "Pero solo veo mi habitación desordenada y una vieja foto de Sayori en mi mesa de noche."
    "¿El cielo es bonito, verdad?..."
    "Me recuerda a ella."
    "A sus ojos llenos de luz."
    "A su sonrisa."
    "A esa voz que hacía parecer más ligeros los días."
    pause 0.5
    "..."
    "Solo quiero que el mundo se detenga un momento."
    "Pero eso es imposible."
    "..."
    scene black
    with fade
    pause 0.5
    "¿Cuándo mi cabeza me dejará en paz?"
    "Hay recuerdos que nunca dejan de volver."
    "..."
    s "'Me gustaría ser como ellos... ¿Crees que algún día pueda?'"
    "Eso es lo que me dijo algún día, en un parque de un caluroso verano."
    "Señalaba a una pareja que se daba mimos."
    "Lastimosamente no recuerdo mi respuesta."
    "He olvidado tantas cosas que ya no sé cuáles ocurrieron realmente."
    pause 0.5    
    "Quiero superar esto."
    pause 0.5
    "..."
    jump .yuri_appears

label .yuri_appears:
    scene bg bedroom
    with dissolve
    # Golpes de puerta
    "Alguien golpea la puerta de mi casa."
    "Mi apariencia no era la adecuada para recibir visitas."
    "Baje la mirada."
    "Llevaba la misma ropa de ayer y no me había duchado."
    "Pero de todas formas abrí la puerta."
    scene bg residential_day
    with fade
    y "B-buenos días..."
    y "Hacía tiempo que no te veía..."
    y "Las chicas del club han estado preocupadas..."
    y "Y... como ahora estamos de vacaciones..."
    y "Pensé que quizá..."
    y "Podía visitarte un rato."
    y "N-no quiero ser una molestia."
    "Yuri..."
    "Ambos mantuvimos una relación amistosa en club."
    "..."
    mc "No te preocupes Yuri, nunca me has molestado."
    "Yuri esboza una sonrisa tímida cuando escucha mi voz."
    "Yo también le devuelvo una sonrisa."
    pause 0.5
    mc "Me alegra que te tomaras el tiempo de venir hasta aquí."
    mc "¿Quisieras pasar a tomar algo de té?"
    mc "Tengo el té de oolong que te gusta."
    y "Ah-ah ¡no no!, de verdad no quiero causar molestias."
    y "De hecho mi intención era saber como estabas [player]."
    y "No es bueno aislarse del mundo."
    y "..."
    y "Se lo difícil que resulta eso."
    mc "..."
    y "Y-yo también extraño a Sayori."
    pause 0.5
    mc "Si..."
    "Ojala todo fuera una pesadilla."
    y "¿No es mi culpa verdad?"
    mc "No, por su puesto que no."
    pause 0.5
    mc "..."
    mc "Verla de esa forma, ver como quedo me resulta inquietante."
    y "Y-yo..."
    y "Lo siento mucho por todo..."
    mc "No tienes que disculparte de nada Yuri."
    "Mi garganta se oprime, miro arriba y exhalo hondo."
    scene bg sky
    with dissolve   
    "El cielo esta despejado."
    "..."
    "Quiero que mis pensamientos sean como este cielo."
    "Limpios, puros y pacíficos."
    y "N-no tienes que pasar por esto solo..."
    "Intenté responder."
    "Pero no salió ninguna palabra."
    "Entonces rompí a llorar."
    y "..."
    y "[player]..."
    pause 0.5
    "Yuri me rodea con sus brazos, apoya su cabeza en mi hombro."
    "Correspondo a su abrazo sin elección."
    y "E-espero que no sea mi culpa..."
    y "Yo..."
    y "De verdad te aprecio mucho [player]."
    y "..."
    y "P-puedes... digo... podemos quedar así el tiempo que quieras."
    "Después de unos segundos, mi llanto se detiene."
    "Y el abrazo también."
    jump .promise_mc

label .promise_mc:
    