USE clinica_dental;

INSERT INTO asistente(idAsistente, nombre, apellido, escolaridad, salario) VALUES(1, 'Marisol', 'Gomez', 'Estudiante de Odontologia', 1000);
INSERT INTO asistente(idAsistente, nombre, apellido, escolaridad, salario) VALUES(2, 'Wendy', 'Perez', 'Estudiante de Odontologia', 1000);
INSERT INTO tipo_especialidad(idTipo_Especialidad, descripcion) VALUES(1, 'Ortodoncista');
INSERT INTO tipo_especialidad(idTipo_Especialidad, descripcion) VALUES(2, 'Anestecista');
INSERT INTO dentista(idDentista, nombre, apellido, numero_telefono, correo_electronico, no_colegiado, Tipo_Especialidad_idTipo_Especialidad) VALUES(1, 'Silvia', 'Soberanis', '65873901', 'dra.silviasoberanis@gmail.com', '12345678', 1);
INSERT INTO dentista(idDentista, nombre, apellido, numero_telefono, correo_electronico, no_colegiado, Tipo_Especialidad_idTipo_Especialidad) VALUES(2, 'Nicthe', 'Castellanos', '65821990', 'nicthe.rodas@gmail.com', '123546578', 2);
INSERT INTO tipo_usuario(idTipo_Usuario, descripcion, permisos) VALUES(1, 'Dentista', 'inventario, ventas, recursos, financiero');
INSERT INTO tipo_usuario(idTipo_Usuario, descripcion, permisos) VALUES(2, 'Asistente', 'inventario, ventas');
INSERT INTO paciente(idPaciente, nombre, apellido, numero_telefonico, correo_electronico, edad, numero_seguro) VALUES(1, 'Edwin', 'Garcia', '34678298', 'edwindavid2002@hotmail.com', 37, '12345');
INSERT INTO paciente(idPaciente, nombre, apellido, numero_telefonico, correo_electronico, edad, numero_seguro) VALUES(2, 'Maria', 'Perez', '346734518', 'mariaperez@gmail.com', 40, '675839');
INSERT INTO cita(idCita, fecha_propuesta, paciente_idPaciente) VALUES(1, '2023-01-14 17:15:00', 1);
INSERT INTO cita(idCita, fecha_propuesta, paciente_idPaciente) VALUES(2, '2023-01-16 05:15:30', 1);
INSERT INTO cita(idCita, fecha_propuesta, paciente_idPaciente) VALUES(3, '2023-01-20 11:00:00', 2);
INSERT INTO tratamiento(idTratamientno, detalle, precio, cantidad_citas, Cita_idCita, Asistente_idAsistente) VALUES (1, "Puente Dental", 2500, 4, 1, 1);
INSERT INTO tratamiento(idTratamientno, detalle, precio, cantidad_citas, Cita_idCita, Asistente_idAsistente) VALUES (2, "Ortodoncia", 300, 10, 2, 1);
INSERT INTO tratamiento(idTratamientno, detalle, precio, cantidad_citas, Cita_idCita, Asistente_idAsistente) VALUES (3, "Limpieza Dental", 100, 1, 3, 2);

ALTER TABLE clinica_dental.material MODIFY COLUMN descripcion VARCHAR(100);
INSERT INTO clinica_dental.material (idMaterial, descripcion, serie_modelo, cantidad, precio_individual) VALUES
(1, 'Yeso', '123ABV', 3, 100),
(2, 'Espejo dental 7/8 pulgadas', 'DTX-VI70041', 3, 10.00),
(3, 'Espejo dental 15/16 pulgadas', 'DTX-VI70042', 3, 10.00),
(4, 'Espejo dental 14 mm', 'DTX-VI70043', 2, 12.00),
(5, 'Explorador simple M', 'M-7EXs3A', 2, 55.26),
(6, 'Explorador simple 1083/6', 'M-7EXs3B', 2, 59.07),
(7, 'Explorador curvo', 'M-7EXs3C', 2, 70.14),
(8, 'Explorador liquid Steel', 'IS1081/70', 2, 66.67),
(9, 'Explorador liquid Steel', 'IS108/33', 4, 84.50),
(10, 'Explorador liquid Steel', 'IS1083/6', 3, 66.16),
(11, 'Explorador Recto', 'IS108/46', 3, 45.00),
(12, 'Palodent Aros Redondos', 'Z-458963', 8, 116.07),
(13, 'Jeringuillas para anestesia dental', 'SDFSASD', 3, 85.00),
(14, 'Pinzas para sistemas de matrices', 'RSS789/5', 2, 632.14),
(15, 'Pinzas para ajuste de brackets 110mm', 'ERTSDF45', 2, 158.94),
(16, 'Pinza Gubia Friedman', 'ERTSDF46', 2, 861.39),
(17, 'Pinzas adson con dientes', 'ERTSDF47', 3, 100.39),
(18, 'Alicates Angulado para crimpar ganchos', 'YRTERT136', 2, 313.07),
(19, 'Alicate para retirar bandas 14cm', 'YRTERT139', 2, 313.07),
(20, 'Sonda de evaluacion de profundidad', 'VIDU', 3, 51.21),
(21, 'Sonda de exploracion doble', 'MEDI', 2, 29.58),
(22, 'Instrumentos de relleno dental compuestos, espatula y puntos de oro titanio', 'COMPOSIKIt', 2, 364.57),
(23, 'Kit de fresas diamantadas', 'DRILLBITS', 2, 150.00),
(24, 'Kit Instrumental dental rotatorio', 'NEXO', 2, 3642.80),
(25, 'Turbina Dental con Conexión Multiflex', 'LOTUS 302 2PK-K', 1, 1419.60),
(26, 'Kit de forcep pk 12 piezas', 'AS-4569772', 2, 800.00),
(27, 'Silla dental', '1.008.0918', 1, 32262.00),
(28, 'Sillas sala de espera', 'Basic Livin silla de espera Meta/plastico', 5, 299.00),
(29, 'Micromotor Marathon 3 dental', 'MARATHON+316', 1, 1550);












