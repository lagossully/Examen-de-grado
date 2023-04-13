--- pregunta 1.3.a
SELECT P.nombre 
FROM Participantes P, ParticipantesYParticipacion PP, Participacion PR, Competencia C, Prueba PU
WHERE P.id = PP.participanteID AND PP.participacionID = PR.id AND PR.tipopruebaID = PU.id AND PU.competenciaID = C.id
AND C.categoria = '40-44' AND PU.distancia = 50 AND PU.estilo = 'E' AND P.genero = 'M'
ORDER BY PP.tiempo ASC
LIMIT 1;

--- pregunta 1.3.b


--- pregunta 2


--- pregunta 3.a

--- pregunta 3.b

--- pregunta 3.c

--- pregunta 3.d