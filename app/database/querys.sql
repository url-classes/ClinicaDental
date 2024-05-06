USE clinica_dental;


INSERT INTO paciente(idPaciente, nombre, apellido, numero_telefonico, correo_electronico, edad, numero_seguro) VALUES(7, 'Edwin', 'Garcia', '34678298', 'edwindavid2002@hotmail.com', 37, '12345');
INSERT INTO paciente(idPaciente, nombre, apellido, numero_telefonico, correo_electronico, edad, numero_seguro) VALUES(8, 'Maria', 'Perez', '346734518', 'mariaperez@gmail.com', 40, '675839');
INSERT INTO paciente(idPaciente, nombre, apellido, numero_telefonico, correo_electronico, edad, numero_seguro) VALUES(9, 'Josue', 'Estrada', '51145070', 'josuebarrios254@gmail.com', 25, '798543');
INSERT INTO paciente(idPaciente, nombre, apellido, numero_telefonico, correo_electronico, edad, numero_seguro) VALUES(10, 'Juan', 'Perez', '47587469', 'jacaceresfuentes@gmail.com', 31, '4587962');
INSERT INTO paciente(idPaciente, nombre, apellido, numero_telefonico, correo_electronico, edad, numero_seguro) VALUES(11, 'Oscar', 'Carrascosa', '34678298', 'oeinteriano@correo.url.edu.gt', 19, '12345');
INSERT INTO paciente(idPaciente, nombre, apellido, numero_telefonico, correo_electronico, edad, numero_seguro) VALUES(12, 'Daniel', 'Interiano', '59530583', 'jdcifuentesca@correo.url.edu.gt', 20, '4783666');
INSERT INTO paciente(idPaciente, nombre, apellido, numero_telefonico, correo_electronico, edad, numero_seguro) VALUES(13, 'Ana', 'Lopez', '54789213', 'analopez@gmail.com', 28, '123456');
INSERT INTO paciente(idPaciente, nombre, apellido, numero_telefonico, correo_electronico, edad, numero_seguro) VALUES(14, 'Luis', 'Martinez', '68745213', 'luis.martinez@hotmail.com', 45, '789012');
INSERT INTO paciente(idPaciente, nombre, apellido, numero_telefonico, correo_electronico, edad, numero_seguro) VALUES(15, 'Elena', 'Gutierrez', '35687412', 'elenagutierrez@yahoo.com', 33, '543219');
INSERT INTO paciente(idPaciente, nombre, apellido, numero_telefonico, correo_electronico, edad, numero_seguro) VALUES(16, 'Pedro', 'Castro', '46892137', 'pedrocastro@gmail.com', 50, '908765');
INSERT INTO paciente(idPaciente, nombre, apellido, numero_telefonico, correo_electronico, edad, numero_seguro) VALUES(17, 'Laura', 'Ramirez', '54783291', 'lauraramirez@hotmail.com', 29, '654321');
INSERT INTO paciente(idPaciente, nombre, apellido, numero_telefonico, correo_electronico, edad, numero_seguro) VALUES(18, 'Sofia', 'Hernandez', '69874321', 'sofiahernandez@yahoo.com', 38, '345678');
INSERT INTO paciente(idPaciente, nombre, apellido, numero_telefonico, correo_electronico, edad, numero_seguro) VALUES(19, 'Carlos', 'Gonzalez', '35678921', 'carlosgonzalez@gmail.com', 27, '987654');
INSERT INTO paciente(idPaciente, nombre, apellido, numero_telefonico, correo_electronico, edad, numero_seguro) VALUES(20, 'Diana', 'Flores', '46872913', 'dianaflores@hotmail.com', 42, '876543');
INSERT INTO paciente(idPaciente, nombre, apellido, numero_telefonico, correo_electronico, edad, numero_seguro) VALUES(21, 'Manuel', 'Sanchez', '54783219', 'manuelsanchez@yahoo.com', 36, '234567');
INSERT INTO paciente(idPaciente, nombre, apellido, numero_telefonico, correo_electronico, edad, numero_seguro) VALUES(22, 'Marta', 'Gomez', '69872143', 'martagomez@gmail.com', 32, '765432');


INSERT INTO cita(idCita, fecha_propuesta, paciente_idPaciente) VALUES(11, '2023-03-15 15:00:00', 11);
INSERT INTO cita(idCita, fecha_propuesta, paciente_idPaciente) VALUES(12, '2023-03-20 17:20:00', 12);
INSERT INTO cita(idCita, fecha_propuesta, paciente_idPaciente) VALUES(13, '2023-04-05 08:00:00', 13);
INSERT INTO cita(idCita, fecha_propuesta, paciente_idPaciente) VALUES(14, '2023-04-10 10:30:00', 14);
INSERT INTO cita(idCita, fecha_propuesta, paciente_idPaciente) VALUES(15, '2023-04-15 12:15:00', 15);
INSERT INTO cita(idCita, fecha_propuesta, paciente_idPaciente) VALUES(16, '2023-04-20 14:40:00', 16);


INSERT INTO tratamiento(idTratamientno, detalle, precio, cantidad_citas, Cita_idCita, Asistente_idAsistente) VALUES (1, "Puente Dental", 2500, 4, 1, 1);
INSERT INTO tratamiento(idTratamientno, detalle, precio, cantidad_citas, Cita_idCita, Asistente_idAsistente) VALUES (2, "Ortodoncia", 300, 10, 2, 1);
INSERT INTO tratamiento(idTratamientno, detalle, precio, cantidad_citas, Cita_idCita, Asistente_idAsistente) VALUES (3, "Limpieza Dental", 350, 1, 3, 2);
INSERT INTO tratamiento(idTratamientno, detalle, precio, cantidad_citas, Cita_idCita, Asistente_idAsistente) VALUES (4, "Brackets", 10000, 20, 4, 1);
INSERT INTO tratamiento(idTratamientno, detalle, precio, cantidad_citas, Cita_idCita, Asistente_idAsistente) VALUES (5, "Implantología dental", 1800, 3, 5, 1);
INSERT INTO tratamiento(idTratamientno, detalle, precio, cantidad_citas, Cita_idCita, Asistente_idAsistente) VALUES (6, "Endodoncia", 800, 2, 6, 2);
INSERT INTO tratamiento(idTratamientno, detalle, precio, cantidad_citas, Cita_idCita, Asistente_idAsistente) VALUES (7, "Blanqueamiento dental", 400, 5, 7, 2);
INSERT INTO tratamiento(idTratamientno, detalle, precio, cantidad_citas, Cita_idCita, Asistente_idAsistente) VALUES (8, "Extracción dental simple", 200, 2, 8, 1);
INSERT INTO tratamiento(idTratamientno, detalle, precio, cantidad_citas, Cita_idCita, Asistente_idAsistente) VALUES (9, "Coronas dentales", 3000, 6, 9, 1);
INSERT INTO tratamiento(idTratamientno, detalle, precio, cantidad_citas, Cita_idCita, Asistente_idAsistente) VALUES (10, "Selladores dentales", 150, 3, 10, 2);
INSERT INTO tratamiento(idTratamientno, detalle, precio, cantidad_citas, Cita_idCita, Asistente_idAsistente) VALUES (11, "Prótesis dental", 4000, 8, 11, 1);
INSERT INTO tratamiento(idTratamientno, detalle, precio, cantidad_citas, Cita_idCita, Asistente_idAsistente) VALUES (12, "Rellenos dentales", 250, 4, 12, 2);
INSERT INTO tratamiento(idTratamientno, detalle, precio, cantidad_citas, Cita_idCita, Asistente_idAsistente) VALUES (13, "Férula de descarga", 600, 2, 13, 1);
INSERT INTO tratamiento(idTratamientno, detalle, precio, cantidad_citas, Cita_idCita, Asistente_idAsistente) VALUES (14, "Extracción de muelas del juicio", 800, 3, 14, 2);
INSERT INTO tratamiento(idTratamientno, detalle, precio, cantidad_citas, Cita_idCita, Asistente_idAsistente) VALUES (15, "Tratamiento de caries", 200, 6, 15, 1);
INSERT INTO tratamiento(idTratamientno, detalle, precio, cantidad_citas, Cita_idCita, Asistente_idAsistente) VALUES (16, "Radiografía dental", 100, 1, 16, 2);



INSERT INTO clinica_dental.material (idMaterial, descripcion, serie_modelo, cantidad, precio_individual) VALUES
(1, 'Yeso', 'Material', 100, 25),
(2, 'Espejo dental 7/8 pulgadas', 'Herramientas', 8, 10.00),
(3, 'Espejo dental 15/16 pulgadas', 'Herramientas', 8, 10.00),
(4, 'Espejo dental 14 mm', 'Herramientas', 6, 12.00),
(5, 'Explorador simple M', 'Herramientas', 6, 55.26),
(6, 'Explorador simple 1083/6', 'Herramientas', 4, 59.07),
(7, 'Explorador curvo', 'Herramientas', 4, 70.14),
(8, 'Explorador liquid Steel', 'Herramientas', 4, 66.67),
(9, 'Explorador liquid Steel', 'Herramientas', 4, 84.50),
(10, 'Explorador liquid Steel', 'Herramientas', 4, 66.16),
(11, 'Explorador Recto', 'Herramientas', 4, 45.00),
(12, 'Palodent Aros Redondos', 'Herramientas', 8, 116.07),
(13, 'Jeringuillas para anestesia dental', 'Material', 200, 85.00),
(14, 'Pinzas para sistemas de matrices', 'Herramientas', 2, 632.14),
(15, 'Pinzas para ajuste de brackets 110mm', 'Herramientas', 2, 158.94),
(16, 'Pinza Gubia Friedman', 'Herramientas', 4, 861.39),
(17, 'Pinzas adson con dientes', 'Herramientas', 4, 100.39),
(18, 'Alicates Angulado para crimpar ganchos', 'Herramientas', 4, 313.07),
(19, 'Alicate para retirar bandas 14cm', 'Herramientas', 2, 313.07),
(20, 'Sonda de evaluacion de profundidad', 'Herramientas', 3, 51.21),
(21, 'Sonda de exploracion doble', 'Herramientas', 2, 29.58),
(22, 'Instrumentos de relleno dental compuestos, espatula y puntos de oro titanio', 'Material', 2, 364.57),
(23, 'Kit de fresas diamantadas', 'Herramientas', 2, 150.00),
(24, 'Kit Instrumental dental rotatorio', 'Herramientas', 2, 3642.80),
(25, 'Turbina Dental con Conexión Multiflex', 'Herramientas', 1, 1419.60),
(26, 'Kit de forcep pk 12 piezas', 'Herramientas', 2, 800.00),
(27, 'Silla dental', 'Herramientas', 1, 32262.00),
(28, 'Sillas sala de espera', 'Herramientas', 5, 299.00),
(29, 'Micromotor Marathon 3 dental', 'Herramientas', 1, 1550),
(30, 'Carillas Composite', 'Material', 50, 320.00),
(31, 'Silicon para impresión dental', 'Material', 2, 962.00),
(32, 'Guantes desechables', 'Material', 200, 2.34),
(33, 'Guantes Quirúrgicos', 'Material', 100, 3.1),
(34, 'Servilletas', 'Material', 1000, 0.05),
(35, 'Brackets', 'Material', 1000, 2.00),
(36, 'Lazos de ligaduras elasticas', 'Material', 100, 31.14),
(37, 'Anestesia lidocaina  ', 'Material', 100, 6.80),
(38, 'Gel anestesico', 'Material', 5, 41.00),
(39, 'Algodon en bolitas', 'Material', 1000, 0.25),
(40, 'Microaplicador dental', 'Material', 500, 0.25),
(41, 'Baberos desechables', 'Material', 500, 0.25),
(42, 'Eyectores de saliva', 'Material', 100, 0.25),
(43, 'Cubre bandejas ', 'Material', 250, 0.25),
(44, 'Gasas de algodon', 'Material', 400, 0.25),
(45, 'Parches absorbente', 'Material', 100, 1.00),
(46, 'Cepillo Dental electrico ', 'Producto', 24, 91.50),
(47, 'Cepillos dentales extra suaves', 'Producto', 24, 39.00),
(48, 'Colgate 360° Luminus', 'Producto', 30, 35.00),
(49, 'Colgate smiles 0-2 años', 'Producto', 30, 38.50),
(50, 'Colgate plax kids', 'Producto', 12, 40.82),
(51, 'Colgate smiles 2-5 años', 'Producto', 24, 48.25),
(52, 'Cepillo dental electrico', 'Producto', 24, 51.60),
(53, 'Hilo dental', 'Producto', 24, 53);




