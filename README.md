<!-- README.md -->
[comment]: # (Inicio de la sección HTML)
<div align="center">

<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Implementación de Métodos de Cifrado en Python</title>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        }
        
        body {
            background: linear-gradient(135deg, #1a2a6c, #2a4d69, #4b86b4);
            color: #f0f8ff;
            line-height: 1.6;
            padding: 20px;
        }
        
        .container {
            max-width: 1000px;
            margin: 0 auto;
            background-color: rgba(13, 27, 42, 0.85);
            border-radius: 15px;
            box-shadow: 0 10px 30px rgba(0, 0, 0, 0.4);
            overflow: hidden;
            border: 1px solid #4b86b4;
        }
        
        header {
            text-align: center;
            padding: 40px 20px;
            background: linear-gradient(to right, #0c1e3e, #1e3c72);
            position: relative;
            overflow: hidden;
        }
        
        header::before {
            content: "";
            position: absolute;
            top: -50%;
            left: -50%;
            width: 200%;
            height: 200%;
            background: radial-gradient(circle, rgba(255,255,255,0.1) 0%, rgba(255,255,255,0) 70%);
            transform: rotate(30deg);
        }
        
        h1 {
            font-size: 2.8rem;
            margin-bottom: 15px;
            position: relative;
            text-shadow: 0 2px 10px rgba(0, 0, 0, 0.5);
        }
        
        .subtitle {
            font-size: 1.4rem;
            max-width: 700px;
            margin: 0 auto 25px;
            color: #a3cef1;
            position: relative;
        }
        
        .badges {
            display: flex;
            justify-content: center;
            gap: 15px;
            margin-top: 20px;
            flex-wrap: wrap;
            position: relative;
        }
        
        .badge {
            background: rgba(74, 107, 136, 0.4);
            padding: 8px 16px;
            border-radius: 20px;
            font-size: 0.9rem;
            border: 1px solid #4b86b4;
            transition: all 0.3s ease;
        }
        
        .badge:hover {
            background: rgba(91, 142, 191, 0.6);
            transform: translateY(-3px);
            box-shadow: 0 5px 15px rgba(0, 0, 0, 0.2);
        }
        
        .content {
            padding: 30px;
        }
        
        .section {
            margin-bottom: 40px;
        }
        
        h2 {
            font-size: 1.8rem;
            margin-bottom: 20px;
            color: #62b6cb;
            padding-bottom: 10px;
            border-bottom: 2px solid #2a6f97;
            position: relative;
        }
        
        h2::after {
            content: "";
            position: absolute;
            bottom: -2px;
            left: 0;
            width: 150px;
            height: 2px;
            background: #62b6cb;
        }
        
        p {
            margin-bottom: 20px;
            font-size: 1.1rem;
        }
        
        .features-grid {
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
            gap: 20px;
        }
        
        .feature-card {
            background: rgba(27, 38, 59, 0.7);
            border-radius: 10px;
            padding: 20px;
            border: 1px solid #2a6f97;
            transition: transform 0.3s ease;
        }
        
        .feature-card:hover {
            transform: translateY(-5px);
            background: rgba(34, 51, 82, 0.8);
        }
        
        .feature-card h3 {
            color: #90e0ef;
            margin-bottom: 15px;
            font-size: 1.3rem;
        }
        
        .algorithms {
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(200px, 1fr));
            gap: 15px;
        }
        
        .algorithm {
            background: rgba(27, 38, 59, 0.7);
            padding: 15px;
            border-radius: 8px;
            text-align: center;
            border: 1px solid #3a506b;
            transition: all 0.3s ease;
        }
        
        .algorithm:hover {
            background: rgba(34, 51, 82, 0.8);
            transform: scale(1.05);
            box-shadow: 0 5px 15px rgba(0, 0, 0, 0.2);
        }
        
        .algorithm-icon {
            font-size: 2rem;
            margin-bottom: 10px;
            color: #90e0ef;
        }
        
        .use-cases {
            display: flex;
            flex-wrap: wrap;
            gap: 15px;
        }
        
        .use-case {
            flex: 1;
            min-width: 200px;
            background: rgba(27, 38, 59, 0.7);
            padding: 20px;
            border-radius: 10px;
            border-left: 4px solid #62b6cb;
        }
        
        .use-case h3 {
            color: #90e0ef;
            margin-bottom: 15px;
        }
        
        footer {
            text-align: center;
            padding: 25px;
            background: rgba(11, 19, 30, 0.8);
            border-top: 1px solid #2a6f97;
            font-size: 0.9rem;
            color: #a3cef1;
        }
        
        @media (max-width: 768px) {
            h1 {
                font-size: 2.2rem;
            }
            
            .subtitle {
                font-size: 1.1rem;
            }
            
            .content {
                padding: 20px;
            }
        }
    </style>
</head>
<body>
    <div class="container">
        <header>
            <h1>Implementación de Métodos de Cifrado en Python</h1>
            <p class="subtitle">Explora algoritmos criptográficos clásicos con implementaciones prácticas y educativas en Python</p>
            <div class="badges">
                <span class="badge">Python 3</span>
                <span class="badge">Criptografía Clásica</span>
                <span class="badge">Seguridad Informática</span>
                <span class="badge">Open Source</span>
            </div>
        </header>
        
        <div class="content">
            <section class="section">
                <h2>Descripción del Proyecto</h2>
                <p>Este repositorio ofrece una colección completa de implementaciones en Python de algoritmos de cifrado históricamente significativos. Cada método demuestra principios fundamentales de criptografía a través de diferentes enfoques matemáticos y técnicos.</p>
                <p>Los algoritmos incluidos van desde cifrados clásicos basados en sustitución y transposición hasta métodos más complejos que utilizan álgebra lineal, operaciones binarias y transformaciones basadas en ASCII para garantizar la confidencialidad de la información.</p>
            </section>
            
            <section class="section">
                <h2>Algoritmos Implementados</h2>
                <div class="algorithms">
                    <div class="algorithm">
                        <div class="algorithm-icon">🔒</div>
                        <h3>Hill</h3>
                        <p>Cifrado basado en matrices y álgebra lineal</p>
                    </div>
                    <div class="algorithm">
                        <div class="algorithm-icon">🔑</div>
                        <h3>Vigenère</h3>
                        <p>Cifrado polialfabético con clave</p>
                    </div>
                    <div class="algorithm">
                        <div class="algorithm-icon">🧩</div>
                        <h3>Playfair</h3>
                        <p>Cifrado de digramas con matriz 5x5</p>
                    </div>
                    <div class="algorithm">
                        <div class="algorithm-icon">🔮</div>
                        <h3>Hermético</h3>
                        <p>Implementación híbrida personalizada</p>
                    </div>
                    <div class="algorithm">
                        <div class="algorithm-icon">🔢</div>
                        <h3>Polybios</h3>
                        <p>Cifrado por sustitución numérica</p>
                    </div>
                    <div class="algorithm">
                        <div class="algorithm-icon">💻</div>
                        <h3>BEYC</h3>
                        <p>Cifrado binario con operaciones lógicas</p>
                    </div>
                    <div class="algorithm">
                        <div class="algorithm-icon">⚡</div>
                        <h3>Vernam</h3>
                        <p>Cifrado de un solo uso (OTP)</p>
                    </div>
                </div>
            </section>
            
            <section class="section">
                <h2>Características Clave</h2>
                <div class="features-grid">
                    <div class="feature-card">
                        <h3>Fundamentos Matemáticos</h3>
                        <p>Demostración de conceptos como álgebra lineal (Hill), aritmética modular (Vigenère) y transformaciones matriciales.</p>
                    </div>
                    <div class="feature-card">
                        <h3>Transformaciones ASCII</h3>
                        <p>Manejo seguro de caracteres mediante conversiones a valores ASCII en varios algoritmos.</p>
                    </div>
                    <div class="feature-card">
                        <h3>Técnicas Híbridas</h3>
                        <p>Combinación de codificación numérica y alfabética en algoritmos como Polybios y BEYC.</p>
                    </div>
                    <div class="feature-card">
                        <h3>Enfoque Educativo</h3>
                        <p>Código bien documentado y comentado, ideal para aprender principios criptográficos.</p>
                    </div>
                    <div class="feature-card">
                        <h3>Implementación Práctica</h3>
                        <p>Scripts ejecutables con ejemplos de entrada/salida para cada algoritmo.</p>
                    </div>
                    <div class="feature-card">
                        <h3>Seguridad Demostrativa</h3>
                        <p>Análisis comparativo de fortalezas y debilidades de cada método criptográfico.</p>
                    </div>
                </div>
            </section>
            
            <section class="section">
                <h2>Casos de Uso</h2>
                <div class="use-cases">
                    <div class="use-case">
                        <h3>🧠 Educación</h3>
                        <p>Recurso ideal para cursos de seguridad informática, criptografía o programación en Python.</p>
                    </div>
                    <div class="use-case">
                        <h3>🔍 Investigación</h3>
                        <p>Base para comparar técnicas criptográficas y analizar su evolución histórica.</p>
                    </div>
                    <div class="use-case">
                        <h3>⚙️ Desarrollo</h3>
                        <p>Código modular fácil de extender para implementar sistemas híbridos modernos.</p>
                    </div>
                </div>
            </section>
        </div>
        
        <footer>
            <p>© 2023 Implementación de Métodos de Cifrado en Python | Proyecto de código abierto para fines educativos</p>
        </footer>
    </div>
</body>
</html>
</div>
[comment]: # (Fin de la sección HTML)
