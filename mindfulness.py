import streamlit as st
import time

def mindfulness_page():
    st.title("Técnicas de Mindfulness y Relajación")
    
    st.markdown("""
    ## Ejercicios de respiración
    
    La respiración consciente es una de las formas más efectivas para reducir el estrés y la ansiedad.
    """)
    
    exercise = st.selectbox(
        "Selecciona un ejercicio de respiración:",
        ["Respiración 4-7-8", "Respiración diafragmática", "Respiración cuadrada"]
    )
    
    if exercise == "Respiración 4-7-8":
        st.markdown("""
        ### Respiración 4-7-8
        
        Esta técnica ayuda a calmar el sistema nervioso:
        
        1. Inhala por la nariz durante 4 segundos
        2. Mantén la respiración durante 7 segundos
        3. Exhala lentamente por la boca durante 8 segundos
        4. Repite el ciclo 4 veces
        """)
        
        if st.button("Iniciar ejercicio guiado de respiración 4-7-8"):
            guided_breathing_478()
    
    elif exercise == "Respiración diafragmática":
        st.markdown("""
        ### Respiración diafragmática
        
        Esta técnica promueve la relajación profunda:
        
        1. Siéntate o acuéstate cómodamente
        2. Coloca una mano en el pecho y otra en el abdomen
        3. Inhala lentamente por la nariz, sintiendo cómo se expande el abdomen
        4. Exhala lentamente por la boca, sintiendo cómo se contrae el abdomen
        5. Repite durante 5-10 minutos
        """)
        
        if st.button("Iniciar ejercicio guiado de respiración diafragmática"):
            guided_breathing_diaphragmatic()
    
    elif exercise == "Respiración cuadrada":
        st.markdown("""
        ### Respiración cuadrada
        
        Esta técnica es excelente para momentos de estrés agudo:
        
        1. Inhala contando hasta 4
        2. Mantén la respiración contando hasta 4
        3. Exhala contando hasta 4
        4. Mantén los pulmones vacíos contando hasta 4
        5. Repite el ciclo
        """)
        
        if st.button("Iniciar ejercicio guiado de respiración cuadrada"):
            guided_breathing_square()
    
    st.markdown("""
    ## Meditación guiada
    
    La meditación regular puede ayudar a reducir el estrés, mejorar la concentración y promover el bienestar general.
    """)
    
    meditation = st.selectbox(
        "Selecciona una meditación guiada:",
        ["Escaneo corporal (5 min)", "Atención plena (10 min)", "Compasión hacia uno mismo (7 min)"]
    )
    
    if meditation == "Escaneo corporal (5 min)":
        st.markdown("""
        ### Escaneo corporal
        
        Esta meditación te ayuda a conectar con tu cuerpo y liberar tensiones:
        
        1. Acuéstate o siéntate en una posición cómoda
        2. Cierra los ojos y respira profundamente
        3. Lleva tu atención a diferentes partes del cuerpo, empezando por los pies
        4. Observa las sensaciones sin juzgarlas
        5. Avanza gradualmente hacia arriba hasta llegar a la cabeza
        """)
        
        if st.button("Iniciar meditación guiada de escaneo corporal"):
            guided_meditation_body_scan()
    
    elif meditation == "Atención plena (10 min)":
        st.markdown("""
        ### Atención plena
        
        Esta meditación te ayuda a centrarte en el momento presente:
        
        1. Siéntate en una posición cómoda con la espalda recta
        2. Enfoca tu atención en la respiración
        3. Cuando tu mente divague, nota el pensamiento sin juzgarlo
        4. Regresa suavemente tu atención a la respiración
        5. Continúa este proceso durante el tiempo designado
        """)
        
        if st.button("Iniciar meditación guiada de atención plena"):
            guided_meditation_mindfulness()
    
    elif meditation == "Compasión hacia uno mismo (7 min)":
        st.markdown("""
        ### Compasión hacia uno mismo
        
        Esta meditación cultiva la amabilidad hacia ti mismo:
        
        1. Siéntate cómodamente y cierra los ojos
        2. Coloca una mano sobre tu corazón
        3. Respira profundamente, sintiendo cómo se expande tu pecho
        4. Repite mentalmente: "Que yo sea amable conmigo mismo"
        5. Continúa con frases de autocompasión
        """)
        
        if st.button("Iniciar meditación guiada de autocompasión"):
            guided_meditation_self_compassion()

def guided_breathing_478():
    placeholder = st.empty()
    
    for i in range(4):  # 4 ciclos
        # Inhalar
        for seconds in range(4, 0, -1):
            placeholder.markdown(f"""
            ## Inhala
            ### {seconds}
            """)
            time.sleep(1)
        
        # Mantener
        for seconds in range(7, 0, -1):
            placeholder.markdown(f"""
            ## Mantén
            ### {seconds}
            """)
            time.sleep(1)
        
        # Exhalar
        for seconds in range(8, 0, -1):
            placeholder.markdown(f"""
            ## Exhala
            ### {seconds}
            """)
            time.sleep(1)
    
    placeholder.markdown("## ¡Ejercicio completado!")
    st.balloons()

def guided_breathing_diaphragmatic():
    placeholder = st.empty()
    
    for i in range(10):  # 10 ciclos
        # Inhalar
        for seconds in range(4, 0, -1):
            placeholder.markdown(f"""
            ## Inhala profundamente por la nariz
            ### Siente cómo se expande tu abdomen
            ### {seconds}
            """)
            time.sleep(1)
        
        # Exhalar
        for seconds in range(6, 0, -1):
            placeholder.markdown(f"""
            ## Exhala lentamente por la boca
            ### Siente cómo se contrae tu abdomen
            ### {seconds}
            """)
            time.sleep(1)
    
    placeholder.markdown("## ¡Ejercicio completado!")
    st.balloons()

def guided_breathing_square():
    placeholder = st.empty()
    
    for i in range(5):  # 5 ciclos
        # Inhalar
        for seconds in range(4, 0, -1):
            placeholder.markdown(f"""
            ## Inhala
            ### {seconds}
            """)
            time.sleep(1)
        
        # Primera retención
        for seconds in range(4, 0, -1):
            placeholder.markdown(f"""
            ## Mantén
            ### {seconds}
            """)
            time.sleep(1)
        
        # Exhalar
        for seconds in range(4, 0, -1):
            placeholder.markdown(f"""
            ## Exhala
            ### {seconds}
            """)
            time.sleep(1)
        
        # Segunda retención
        for seconds in range(4, 0, -1):
            placeholder.markdown(f"""
            ## Mantén (pulmones vacíos)
            ### {seconds}
            """)
            time.sleep(1)
    
    placeholder.markdown("## ¡Ejercicio completado!")
    st.balloons()

def guided_meditation_body_scan():
    placeholder = st.empty()
    
    # Introducción
    placeholder.markdown("""
    ## Escaneo Corporal
    
    Ponte cómodo y cierra los ojos. Vamos a comenzar...
    """)
    time.sleep(5)
    
    # Partes del cuerpo
    body_parts = [
        ("pies", "Siente cualquier sensación en tus pies. Nota si hay tensión o relajación."),
        ("piernas", "Lleva tu atención a tus piernas. Observa cualquier sensación presente."),
        ("abdomen", "Siente tu abdomen subir y bajar con cada respiración."),
        ("pecho", "Observa tu pecho y cualquier sensación alrededor del corazón."),
        ("manos", "Lleva tu atención a tus manos. Nota cualquier hormigueo o calor."),
        ("brazos", "Siente tus brazos. Observa si hay tensión o pesadez."),
        ("hombros", "Observa tus hombros. Permite que cualquier tensión se disuelva."),
        ("cuello", "Lleva tu atención al cuello. Relaja cualquier tensión que encuentres."),
        ("rostro", "Observa tu rostro. Relaja la mandíbula, los ojos y la frente."),
        ("cabeza", "Finalmente, lleva tu atención a la parte superior de tu cabeza.")
    ]
    
    for part, instruction in body_parts:
        placeholder.markdown(f"""
        ## {part.capitalize()}
        
        {instruction}
        """)
        time.sleep(30)
    
    # Conclusión
    placeholder.markdown("""
    ## Terminando la meditación
    
    Toma conciencia de todo tu cuerpo como una unidad completa.
    Respira profundamente y, cuando estés listo, abre lentamente los ojos.
    """)
    time.sleep(5)
    
    placeholder.markdown("## ¡Meditación completada!")
    st.balloons()

def guided_meditation_mindfulness():
    placeholder = st.empty()
    
    # Introducción
    placeholder.markdown("""
    ## Meditación de Atención Plena
    
    Siéntate cómodamente con la espalda recta. Vamos a comenzar...
    """)
    time.sleep(5)
    
    # Instrucciones
    instructions = [
        "Cierra los ojos y toma tres respiraciones profundas.",
        "Lleva tu atención a la sensación de tu respiración. Nota cómo entra y sale el aire.",
        "Si tu mente divaga, simplemente nota dónde fue y regresa suavemente a la respiración.",
        "Observa las sensaciones físicas en tu cuerpo mientras respiras.",
        "Nota los sonidos a tu alrededor sin juzgarlos.",
        "Observa tus pensamientos como si fueran nubes pasando por el cielo.",
        "Regresa a la respiración como tu ancla al momento presente.",
        "Expande tu conciencia para incluir todo tu cuerpo.",
        "Nota cómo te sientes en este momento, sin intentar cambiar nada.",
        "Prepárate para terminar la meditación, manteniendo esta conciencia contigo."
    ]
    
    for i, instruction in enumerate(instructions):
        placeholder.markdown(f"""
        ## Paso {i+1}
        
        {instruction}
        """)
        time.sleep(60)  # 1 minuto por instrucción
    
    # Conclusión
    placeholder.markdown("""
    ## Terminando la meditación
    
    Toma una respiración profunda. Cuando estés listo, abre lentamente los ojos.
    """)
    time.sleep(5)
    
    placeholder.markdown("## ¡Meditación completada!")
    st.balloons()

def guided_meditation_self_compassion():
    placeholder = st.empty()
    
    # Introducción
    placeholder.markdown("""
    ## Meditación de Autocompasión
    
    Siéntate cómodamente y coloca una mano sobre tu corazón. Vamos a comenzar...
    """)
    time.sleep(5)
    
    # Frases de autocompasión
    phrases = [
        "Que yo sea amable conmigo mismo.",
        "Que yo me acepte tal como soy.",
        "Que yo me dé la compasión que necesito.",
        "Que yo sea paciente con mis dificultades.",
        "Que yo me perdone por mis errores.",
        "Que yo reconozca mi valor inherente.",
        "Que yo me trate con la misma amabilidad que ofrezco a los demás."
    ]
    
    for i, phrase in enumerate(phrases):
        placeholder.markdown(f"""
        ## Repite mentalmente:
        
        ### "{phrase}"
        
        Respira profundamente y siente las palabras en tu corazón.
        """)
        time.sleep(60)  # 1 minuto por frase
    
    # Conclusión
    placeholder.markdown("""
    ## Terminando la meditación
    
    Toma una respiración profunda. Lleva contigo esta sensación de autocompasión.
    Cuando estés listo, abre lentamente los ojos.
    """)
    time.sleep(5)
    
    placeholder.markdown("## ¡Meditación completada!")
    st.balloons()

if __name__ == "__main__":
    mindfulness_page() 