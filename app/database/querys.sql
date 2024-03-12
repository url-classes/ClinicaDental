USE clinica_dental;
INSERT INTO material(idMaterial, descripcion, serie_modelo, cantidad, precio_individual) VALUES (1, 'Yeso', '123ABV', 3, 100);
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











