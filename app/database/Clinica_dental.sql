-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema clinica_dental
-- -----------------------------------------------------
DROP SCHEMA IF EXISTS `clinica_dental` ;

-- -----------------------------------------------------
-- Schema clinica_dental
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `clinica_dental` DEFAULT CHARACTER SET utf8mb4 ;
USE `clinica_dental` ;

-- -----------------------------------------------------
-- Table `clinica_dental`.`alergia`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `clinica_dental`.`alergia` (
  `idAlergia` INT(11) NOT NULL AUTO_INCREMENT,
  `descripcion` VARCHAR(45) NULL DEFAULT NULL,
  PRIMARY KEY (`idAlergia`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4;


-- -----------------------------------------------------
-- Table `clinica_dental`.`paciente`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `clinica_dental`.`paciente` (
  `idPaciente` INT(11) NOT NULL AUTO_INCREMENT,
  `nombre` VARCHAR(45) NULL DEFAULT NULL,
  `apellido` VARCHAR(45) NULL DEFAULT NULL,
  `numero_telefonico` VARCHAR(45) NULL DEFAULT NULL,
  `correo_electronico` VARCHAR(45) NULL DEFAULT NULL,
  `edad` INT(11) NULL DEFAULT NULL,
  `numero_seguro` VARCHAR(45) NULL DEFAULT NULL,
  `ultima_visita` DATETIME NULL DEFAULT NULL,
  PRIMARY KEY (`idPaciente`))
ENGINE = InnoDB
AUTO_INCREMENT = 6
DEFAULT CHARACTER SET = utf8mb4;


-- -----------------------------------------------------
-- Table `clinica_dental`.`alergia_paciente`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `clinica_dental`.`alergia_paciente` (
  `Alergia_idAlergia` INT(11) NOT NULL,
  `Paciente_idPaciente` INT(11) NOT NULL,
  PRIMARY KEY (`Alergia_idAlergia`, `Paciente_idPaciente`),
  INDEX `fk_Alergia_has_Paciente_Paciente1_idx` (`Paciente_idPaciente` ASC) VISIBLE,
  INDEX `fk_Alergia_has_Paciente_Alergia1_idx` (`Alergia_idAlergia` ASC) VISIBLE,
  CONSTRAINT `fk_Alergia_has_Paciente_Alergia1`
    FOREIGN KEY (`Alergia_idAlergia`)
    REFERENCES `clinica_dental`.`alergia` (`idAlergia`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Alergia_has_Paciente_Paciente1`
    FOREIGN KEY (`Paciente_idPaciente`)
    REFERENCES `clinica_dental`.`paciente` (`idPaciente`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4;


-- -----------------------------------------------------
-- Table `clinica_dental`.`asistente`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `clinica_dental`.`asistente` (
  `idAsistente` INT(11) NOT NULL AUTO_INCREMENT,
  `nombre` VARCHAR(45) NULL DEFAULT NULL,
  `apellido` VARCHAR(45) NULL DEFAULT NULL,
  `escolaridad` VARCHAR(45) NULL DEFAULT NULL,
  `salario` FLOAT NULL DEFAULT NULL,
  `estado` TINYINT(1) NULL,
  `url` VARCHAR(100) NULL,
  PRIMARY KEY (`idAsistente`))
ENGINE = InnoDB
AUTO_INCREMENT = 7
DEFAULT CHARACTER SET = utf8mb4;


-- -----------------------------------------------------
-- Table `clinica_dental`.`cita`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `clinica_dental`.`cita` (
  `idCita` INT(11) NOT NULL AUTO_INCREMENT,
  `fecha_propuesta` DATETIME NULL DEFAULT NULL,
  `estado` TINYINT(1) NULL DEFAULT 1,
  `paciente_idPaciente` INT(11) NOT NULL,
  PRIMARY KEY (`idCita`),
  INDEX `fk_cita_paciente1_idx` (`paciente_idPaciente` ASC) VISIBLE,
  CONSTRAINT `fk_cita_paciente1`
    FOREIGN KEY (`paciente_idPaciente`)
    REFERENCES `clinica_dental`.`paciente` (`idPaciente`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB
AUTO_INCREMENT = 10
DEFAULT CHARACTER SET = utf8mb4;


-- -----------------------------------------------------
-- Table `clinica_dental`.`tipo_especialidad`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `clinica_dental`.`tipo_especialidad` (
  `idTipo_Especialidad` INT(11) NOT NULL AUTO_INCREMENT,
  `descripcion` VARCHAR(45) NULL DEFAULT NULL,
  PRIMARY KEY (`idTipo_Especialidad`))
ENGINE = InnoDB
AUTO_INCREMENT = 7
DEFAULT CHARACTER SET = utf8mb4;


-- -----------------------------------------------------
-- Table `clinica_dental`.`dentista`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `clinica_dental`.`dentista` (
  `idDentista` INT(11) NOT NULL AUTO_INCREMENT,
  `nombre` VARCHAR(45) NULL DEFAULT NULL,
  `apellido` VARCHAR(45) NULL DEFAULT NULL,
  `numero_telefono` VARCHAR(45) NULL DEFAULT NULL,
  `correo_electronico` VARCHAR(45) NULL DEFAULT NULL,
  `no_colegiado` VARCHAR(45) NULL DEFAULT NULL,
  `estado` TINYINT(1) NULL,
  `url` VARCHAR(100) NULL,
  `Tipo_Especialidad_idTipo_Especialidad` INT(11) NOT NULL,
  PRIMARY KEY (`idDentista`),
  INDEX `fk_Dentista_Tipo_Especialidad1_idx` (`Tipo_Especialidad_idTipo_Especialidad` ASC) VISIBLE,
  CONSTRAINT `fk_Dentista_Tipo_Especialidad1`
    FOREIGN KEY (`Tipo_Especialidad_idTipo_Especialidad`)
    REFERENCES `clinica_dental`.`tipo_especialidad` (`idTipo_Especialidad`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB
AUTO_INCREMENT = 8
DEFAULT CHARACTER SET = utf8mb4;


-- -----------------------------------------------------
-- Table `clinica_dental`.`tratamiento`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `clinica_dental`.`tratamiento` (
  `idTratamientno` INT(11) NOT NULL AUTO_INCREMENT,
  `detalle` VARCHAR(45) NULL DEFAULT NULL,
  `precio` FLOAT NULL DEFAULT NULL,
  `cantidad_citas` INT(11) NULL DEFAULT NULL,
  `estado` TINYINT(1) NULL,
  `Cita_idCita` INT(11) NOT NULL,
  `Asistente_idAsistente` INT(11) NOT NULL,
  PRIMARY KEY (`idTratamientno`),
  INDEX `fk_Tratamiento_Cita1_idx` (`Cita_idCita` ASC) VISIBLE,
  INDEX `fk_Tratamiento_Asistente1_idx` (`Asistente_idAsistente` ASC) VISIBLE,
  CONSTRAINT `fk_Tratamiento_Asistente1`
    FOREIGN KEY (`Asistente_idAsistente`)
    REFERENCES `clinica_dental`.`asistente` (`idAsistente`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Tratamiento_Cita1`
    FOREIGN KEY (`Cita_idCita`)
    REFERENCES `clinica_dental`.`cita` (`idCita`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB
AUTO_INCREMENT = 6
DEFAULT CHARACTER SET = utf8mb4;


-- -----------------------------------------------------
-- Table `clinica_dental`.`dentista_tratamiento`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `clinica_dental`.`dentista_tratamiento` (
  `Dentista_idDentista` INT(11) NOT NULL,
  `Tratamiento_idTratamientno` INT(11) NOT NULL,
  PRIMARY KEY (`Dentista_idDentista`, `Tratamiento_idTratamientno`),
  INDEX `fk_Dentista_has_Tratamiento_Tratamiento1_idx` (`Tratamiento_idTratamientno` ASC) VISIBLE,
  INDEX `fk_Dentista_has_Tratamiento_Dentista1_idx` (`Dentista_idDentista` ASC) VISIBLE,
  CONSTRAINT `fk_Dentista_has_Tratamiento_Dentista1`
    FOREIGN KEY (`Dentista_idDentista`)
    REFERENCES `clinica_dental`.`dentista` (`idDentista`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Dentista_has_Tratamiento_Tratamiento1`
    FOREIGN KEY (`Tratamiento_idTratamientno`)
    REFERENCES `clinica_dental`.`tratamiento` (`idTratamientno`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4;


-- -----------------------------------------------------
-- Table `clinica_dental`.`factura`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `clinica_dental`.`factura` (
  `idFactura` INT(11) NOT NULL AUTO_INCREMENT,
  `detalle` VARCHAR(45) NULL DEFAULT NULL,
  `cantidad_servicios` INT(11) NULL DEFAULT NULL,
  `fecha` DATETIME NULL DEFAULT NULL,
  `total` FLOAT NULL DEFAULT NULL,
  `Tratamiento_idTratamientno` INT(11) NOT NULL,
  PRIMARY KEY (`idFactura`),
  INDEX `fk_Factura_Tratamiento1_idx` (`Tratamiento_idTratamientno` ASC) VISIBLE,
  CONSTRAINT `fk_Factura_Tratamiento1`
    FOREIGN KEY (`Tratamiento_idTratamientno`)
    REFERENCES `clinica_dental`.`tratamiento` (`idTratamientno`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4;


-- -----------------------------------------------------
-- Table `clinica_dental`.`material`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `clinica_dental`.`material` (
  `idMaterial` INT(11) NOT NULL AUTO_INCREMENT,
  `descripcion` VARCHAR(100) NULL DEFAULT NULL,
  `serie_modelo` VARCHAR(45) NULL DEFAULT NULL,
  `cantidad` INT(11) NULL DEFAULT NULL,
  `precio_individual` FLOAT NULL DEFAULT NULL,
  `estado` TINYINT(1) NULL,
  PRIMARY KEY (`idMaterial`))
ENGINE = InnoDB
AUTO_INCREMENT = 11
DEFAULT CHARACTER SET = utf8mb4;


-- -----------------------------------------------------
-- Table `clinica_dental`.`tipo_usuario`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `clinica_dental`.`tipo_usuario` (
  `idTipo_Usuario` INT(11) NOT NULL AUTO_INCREMENT,
  `descripcion` VARCHAR(45) NULL DEFAULT NULL,
  `permisos` VARCHAR(45) NULL DEFAULT NULL,
  PRIMARY KEY (`idTipo_Usuario`))
ENGINE = InnoDB
AUTO_INCREMENT = 9
DEFAULT CHARACTER SET = utf8mb4;


-- -----------------------------------------------------
-- Table `clinica_dental`.`tratamiento_material`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `clinica_dental`.`tratamiento_material` (
  `id` INT(11) NOT NULL AUTO_INCREMENT,
  `Tratamiento_idTratamientno` INT(11) NOT NULL,
  `Material_idMaterial` INT(11) NOT NULL,
  `cantidad_utilizada` INT(11) NULL DEFAULT NULL,
  `cantidad_antes` INT NULL,
  `cantidad_despues` INT NULL,
  `fecha_transaccion` DATETIME NULL,
  PRIMARY KEY (`id`),  -- Clave primaria basada en `id`
  INDEX `fk_Tratamiento_has_Material_Material1_idx` (`Material_idMaterial` ASC) VISIBLE,
  INDEX `fk_Tratamiento_has_Material_Tratamiento1_idx` (`Tratamiento_idTratamientno` ASC) VISIBLE,
  CONSTRAINT `fk_Tratamiento_has_Material_Material1`
    FOREIGN KEY (`Material_idMaterial`)
    REFERENCES `clinica_dental`.`material` (`idMaterial`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Tratamiento_has_Material_Tratamiento1`
    FOREIGN KEY (`Tratamiento_idTratamientno`)
    REFERENCES `clinica_dental`.`tratamiento` (`idTratamientno`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4;


-- -----------------------------------------------------
-- Table `clinica_dental`.`usuario`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `clinica_dental`.`usuario` (
  `idUsuario` INT(11) NOT NULL AUTO_INCREMENT,
  `nombre_usuario` VARCHAR(45) NOT NULL,
  `password` VARCHAR(255) NULL DEFAULT NULL,
  `last_login` DATETIME NULL DEFAULT NULL,
  `intentos_fallidos` INT NULL DEFAULT 0,
  `tiempo_bloqueo` DATETIME NULL DEFAULT NULL,
  `Dentista_idDentista` INT(11) NULL DEFAULT NULL,
  `Tipo_Usuario_idTipo_Usuario` INT(11) NOT NULL,
  `Asistente_idAsistente` INT(11) NULL DEFAULT NULL,
  PRIMARY KEY (`idUsuario`),
  INDEX `fk_Usuario_Dentista1_idx` (`Dentista_idDentista` ASC) VISIBLE,
  INDEX `fk_Usuario_Tipo_Usuario1_idx` (`Tipo_Usuario_idTipo_Usuario` ASC) VISIBLE,
  INDEX `fk_Usuario_Asistente1_idx` (`Asistente_idAsistente` ASC) VISIBLE,
  CONSTRAINT `fk_Usuario_Asistente1`
    FOREIGN KEY (`Asistente_idAsistente`)
    REFERENCES `clinica_dental`.`asistente` (`idAsistente`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Usuario_Dentista1`
    FOREIGN KEY (`Dentista_idDentista`)
    REFERENCES `clinica_dental`.`dentista` (`idDentista`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Usuario_Tipo_Usuario1`
    FOREIGN KEY (`Tipo_Usuario_idTipo_Usuario`)
    REFERENCES `clinica_dental`.`tipo_usuario` (`idTipo_Usuario`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB
AUTO_INCREMENT = 6
DEFAULT CHARACTER SET = utf8mb4;

USE `clinica_dental` ;

-- -----------------------------------------------------
-- procedure RegistrarCita
-- -----------------------------------------------------

DELIMITER $$
USE `clinica_dental`$$
CREATE PROCEDURE RegistrarCita(
    IN fechaPropuesta DATETIME,
    IN idPaciente INT,
    IN idDentista INT
)
BEGIN
    DECLARE estadoPaciente TINYINT;
    DECLARE estadoDentista TINYINT;

    -- Verificar estado del paciente
    SELECT estado INTO estadoPaciente FROM clinica_dental.paciente WHERE idPaciente = idPaciente;
    -- Verificar estado del dentista
    SELECT estado INTO estadoDentista FROM clinica_dental.dentista WHERE idDentista = idDentista;

    IF estadoPaciente = 1 AND estadoDentista = 1 THEN
        -- Ambos están activos, se puede proceder a insertar la cita
        INSERT INTO clinica_dental.cita(fecha_propuesta, estado, paciente_idPaciente, dentista_idDentista)
        VALUES (fechaPropuesta, 1, idPaciente, idDentista);
    ELSE
        -- Uno o ambos están inactivos, no se inserta la cita y se lanza un error
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'El paciente o dentista no está activo';
    END IF;
END$$

DELIMITER ;

-- -----------------------------------------------------
-- procedure verificarIngreso
-- -----------------------------------------------------

DELIMITER $$
USE `clinica_dental`$$
CREATE PROCEDURE verificarIngreso(IN usuario_id INT, IN contrasena_proveida VARCHAR(255))
BEGIN
    DECLARE contrasena_actual VARCHAR(255);
    DECLARE fallos INT;
    DECLARE tiempo DATETIME;

    -- Extrae la contraseña actual, los intentos fallidos actuales y el tiempo de bloqueo
    SELECT contrasena, intentos_fallidos, tiempo_bloqueo INTO contrasena_actual, fallos, tiempo
    FROM usuario WHERE idUsuario = usuario_id;

    -- Verifica si el tiempo actual es menor que el tiempo de bloqueo
    IF NOW() < tiempo THEN
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Debe esperar 1 minuto antes de volver a intentar';
    ELSEIF contrasena_actual = contrasena_proveida THEN
        -- Si la contraseña es correcta, resetea los intentos fallidos y el tiempo de bloqueo
        UPDATE usuario SET intentos_fallidos = 0, tiempo_bloqueo = NULL WHERE idUsuario = usuario_id;
    ELSE
        -- Incrementa los intentos fallidos y establece el tiempo de bloqueo si es necesario
        UPDATE usuario
        SET intentos_fallidos = fallos + 1,
            tiempo_bloqueo = IF(fallos + 1 >= 5, DATE_ADD(NOW(), INTERVAL 1 MINUTE), NULL)
        WHERE idUsuario = usuario_id;

        -- Comprueba si se ha alcanzado el límite de intentos fallidos
        IF fallos + 1 >= 5 THEN
            SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Ha superado el número de intentos. Espere 1 minuto.';
        ELSE
            SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Contraseña incorrecta. Intente de nuevo.';
        END IF;
    END IF;
END$$

DELIMITER ;
USE `clinica_dental`;

DELIMITER $$
USE `clinica_dental`$$
CREATE TRIGGER ActualizarUltimaVisita
AFTER INSERT ON clinica_dental.cita
FOR EACH ROW
BEGIN
    UPDATE clinica_dental.paciente
    SET ultima_visita = NEW.fecha_propuesta
    WHERE idPaciente = NEW.paciente_idPaciente;
END;$$

USE `clinica_dental`$$
CREATE TRIGGER VerificarMaterialAntesTratamiento
BEFORE INSERT ON clinica_dental.tratamiento_material
FOR EACH ROW
BEGIN
    DECLARE materialDisponible INT;
    SELECT cantidad INTO materialDisponible FROM clinica_dental.material
    WHERE idMaterial = NEW.Material_idMaterial;

    IF materialDisponible < NEW.cantidad_utilizada THEN
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'No hay suficiente material en stock';
    END IF;
END$$

USE `clinica_dental`$$
CREATE TRIGGER ActualizarCantidadMaterial
AFTER INSERT ON clinica_dental.tratamiento_material
FOR EACH ROW
BEGIN
    UPDATE clinica_dental.material
    SET cantidad = NEW.cantidad_despues
    WHERE idMaterial = NEW.Material_idMaterial;
END$$


DELIMITER ;

SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;

-- -----------------------------------------------------
-- Data for table `clinica_dental`.`alergia`
-- -----------------------------------------------------
START TRANSACTION;
USE `clinica_dental`;
INSERT INTO `clinica_dental`.`alergia` (`idAlergia`, `descripcion`) VALUES (1, 'Ninguna');
INSERT INTO `clinica_dental`.`alergia` (`idAlergia`, `descripcion`) VALUES (2, 'Asma alérgico');
INSERT INTO `clinica_dental`.`alergia` (`idAlergia`, `descripcion`) VALUES (3, 'Dermatitis atópica');
INSERT INTO `clinica_dental`.`alergia` (`idAlergia`, `descripcion`) VALUES (4, 'Rinitis alérgica');
INSERT INTO `clinica_dental`.`alergia` (`idAlergia`, `descripcion`) VALUES (5, 'Urticaria crónica');
INSERT INTO `clinica_dental`.`alergia` (`idAlergia`, `descripcion`) VALUES (6, 'Poliposis nasal');
INSERT INTO `clinica_dental`.`alergia` (`idAlergia`, `descripcion`) VALUES (7, 'Anticonvulsivos');
INSERT INTO `clinica_dental`.`alergia` (`idAlergia`, `descripcion`) VALUES (8, 'Penicilina');
INSERT INTO `clinica_dental`.`alergia` (`idAlergia`, `descripcion`) VALUES (9, 'Insulina');
INSERT INTO `clinica_dental`.`alergia` (`idAlergia`, `descripcion`) VALUES (10, 'Sustancias que contenga yodo');

COMMIT;


-- -----------------------------------------------------
-- Data for table `clinica_dental`.`paciente`
-- -----------------------------------------------------
START TRANSACTION;
USE `clinica_dental`;
INSERT INTO `clinica_dental`.`paciente` (`idPaciente`, `nombre`, `apellido`, `numero_telefonico`, `correo_electronico`, `edad`, `numero_seguro`, `ultima_visita`) VALUES (1, 'Edwin', 'Garcia', '34678298', 'edwindavid2002@hotmail.com', 37, '12345', NULL);
INSERT INTO `clinica_dental`.`paciente` (`idPaciente`, `nombre`, `apellido`, `numero_telefonico`, `correo_electronico`, `edad`, `numero_seguro`, `ultima_visita`) VALUES (2, 'Maria', 'Perez', '34323234', 'mariaperez@gmail.com', 53, '54354', NULL);
INSERT INTO `clinica_dental`.`paciente` (`idPaciente`, `nombre`, `apellido`, `numero_telefonico`, `correo_electronico`, `edad`, `numero_seguro`, `ultima_visita`) VALUES (3, 'Josue', 'Estrada', '8786786', 'josuebarrios254@gmail.com', 23, '534534', NULL);
INSERT INTO `clinica_dental`.`paciente` (`idPaciente`, `nombre`, `apellido`, `numero_telefonico`, `correo_electronico`, `edad`, `numero_seguro`, `ultima_visita`) VALUES (4, 'Juan', 'Perez', '234234', 'jacaceresfuentes@gmail.com', 77, '213023213', NULL);
INSERT INTO `clinica_dental`.`paciente` (`idPaciente`, `nombre`, `apellido`, `numero_telefonico`, `correo_electronico`, `edad`, `numero_seguro`, `ultima_visita`) VALUES (5, 'Oscar', 'Carrascosa', '78787809', 'jdcifuentesca@correo.url.edu.g', 86, '234324', NULL);
INSERT INTO `clinica_dental`.`paciente` (`idPaciente`, `nombre`, `apellido`, `numero_telefonico`, `correo_electronico`, `edad`, `numero_seguro`, `ultima_visita`) VALUES (6, 'Romina', 'Hernandez', '123124432', 'romina.hernandez@gmail.com', 43, '34234', NULL);

COMMIT;


-- -----------------------------------------------------
-- Data for table `clinica_dental`.`alergia_paciente`
-- -----------------------------------------------------
START TRANSACTION;
USE `clinica_dental`;
INSERT INTO `clinica_dental`.`alergia_paciente` (`Alergia_idAlergia`, `Paciente_idPaciente`) VALUES (1, 1);
INSERT INTO `clinica_dental`.`alergia_paciente` (`Alergia_idAlergia`, `Paciente_idPaciente`) VALUES (1, 2);
INSERT INTO `clinica_dental`.`alergia_paciente` (`Alergia_idAlergia`, `Paciente_idPaciente`) VALUES (4, 3);
INSERT INTO `clinica_dental`.`alergia_paciente` (`Alergia_idAlergia`, `Paciente_idPaciente`) VALUES (5, 4);
INSERT INTO `clinica_dental`.`alergia_paciente` (`Alergia_idAlergia`, `Paciente_idPaciente`) VALUES (2, 5);
INSERT INTO `clinica_dental`.`alergia_paciente` (`Alergia_idAlergia`, `Paciente_idPaciente`) VALUES (3, 6);

COMMIT;


-- -----------------------------------------------------
-- Data for table `clinica_dental`.`asistente`
-- -----------------------------------------------------
START TRANSACTION;
USE `clinica_dental`;
INSERT INTO `clinica_dental`.`asistente` (`idAsistente`, `nombre`, `apellido`, `escolaridad`, `salario`, `estado`, `url`) VALUES (1, 'Marisol', 'Gomez', 'Estudiante de Odontologia', 1000, 1, NULL);
INSERT INTO `clinica_dental`.`asistente` (`idAsistente`, `nombre`, `apellido`, `escolaridad`, `salario`, `estado`, `url`) VALUES (2, 'Wendy', 'Perez', 'Estudiante de Odontologia', 1000, 1, NULL);
INSERT INTO `clinica_dental`.`asistente` (`idAsistente`, `nombre`, `apellido`, `escolaridad`, `salario`, `estado`, `url`) VALUES (3, 'Sofia', 'Chaves', 'Estudiante de Odontologia', 1000, 1, NULL);
INSERT INTO `clinica_dental`.`asistente` (`idAsistente`, `nombre`, `apellido`, `escolaridad`, `salario`, `estado`, `url`) VALUES (4, 'Armando', 'Sosa', 'Estudiante de Odontologia', 1000, 1, NULL);

COMMIT;


-- -----------------------------------------------------
-- Data for table `clinica_dental`.`cita`
-- -----------------------------------------------------
START TRANSACTION;
USE `clinica_dental`;
INSERT INTO `clinica_dental`.`cita` (`idCita`, `fecha_propuesta`, `estado`, `paciente_idPaciente`) VALUES (1, '2023-01-14 17:15:00', 1, 1);
INSERT INTO `clinica_dental`.`cita` (`idCita`, `fecha_propuesta`, `estado`, `paciente_idPaciente`) VALUES (2, '2023-01-16 05:15:30', 1, 2);
INSERT INTO `clinica_dental`.`cita` (`idCita`, `fecha_propuesta`, `estado`, `paciente_idPaciente`) VALUES (3, '2023-01-20 11:00:00', 1, 3);
INSERT INTO `clinica_dental`.`cita` (`idCita`, `fecha_propuesta`, `estado`, `paciente_idPaciente`) VALUES (4, '2023-01-25 14:30:0', 1, 4);
INSERT INTO `clinica_dental`.`cita` (`idCita`, `fecha_propuesta`, `estado`, `paciente_idPaciente`) VALUES (5, '2023-02-05 10:45:00', 1, 5);
INSERT INTO `clinica_dental`.`cita` (`idCita`, `fecha_propuesta`, `estado`, `paciente_idPaciente`) VALUES (6, '2023-02-10 09:00:00', 1, 1);
INSERT INTO `clinica_dental`.`cita` (`idCita`, `fecha_propuesta`, `estado`, `paciente_idPaciente`) VALUES (7, '2023-02-15 13:20:00', 1, 2);
INSERT INTO `clinica_dental`.`cita` (`idCita`, `fecha_propuesta`, `estado`, `paciente_idPaciente`) VALUES (8, '2023-02-20 16:10:00', 1, 3);
INSERT INTO `clinica_dental`.`cita` (`idCita`, `fecha_propuesta`, `estado`, `paciente_idPaciente`) VALUES (9, '2023-03-05 08:30:00', 1, 4);
INSERT INTO `clinica_dental`.`cita` (`idCita`, `fecha_propuesta`, `estado`, `paciente_idPaciente`) VALUES (10, '2023-03-10 11:45:00', 1, 5);

COMMIT;


-- -----------------------------------------------------
-- Data for table `clinica_dental`.`tipo_especialidad`
-- -----------------------------------------------------
START TRANSACTION;
USE `clinica_dental`;
INSERT INTO `clinica_dental`.`tipo_especialidad` (`idTipo_Especialidad`, `descripcion`) VALUES (1, 'Dentista genera');
INSERT INTO `clinica_dental`.`tipo_especialidad` (`idTipo_Especialidad`, `descripcion`) VALUES (2, 'Odontopediatra');
INSERT INTO `clinica_dental`.`tipo_especialidad` (`idTipo_Especialidad`, `descripcion`) VALUES (3, 'Ortodoncista');
INSERT INTO `clinica_dental`.`tipo_especialidad` (`idTipo_Especialidad`, `descripcion`) VALUES (4, 'Periodoncista');
INSERT INTO `clinica_dental`.`tipo_especialidad` (`idTipo_Especialidad`, `descripcion`) VALUES (5, 'Endodoncista');
INSERT INTO `clinica_dental`.`tipo_especialidad` (`idTipo_Especialidad`, `descripcion`) VALUES (6, 'Patólogo oral');
INSERT INTO `clinica_dental`.`tipo_especialidad` (`idTipo_Especialidad`, `descripcion`) VALUES (7, 'Prostodoncista');

COMMIT;


-- -----------------------------------------------------
-- Data for table `clinica_dental`.`dentista`
-- -----------------------------------------------------
START TRANSACTION;
USE `clinica_dental`;
INSERT INTO `clinica_dental`.`dentista` (`idDentista`, `nombre`, `apellido`, `numero_telefono`, `correo_electronico`, `no_colegiado`, `estado`, `url`, `Tipo_Especialidad_idTipo_Especialidad`) VALUES (1, 'Silvia', 'Soberanis', '65873901', 'dra.silviasoberanis@gmail.com', '12345678', 1, NULL, 2);
INSERT INTO `clinica_dental`.`dentista` (`idDentista`, `nombre`, `apellido`, `numero_telefono`, `correo_electronico`, `no_colegiado`, `estado`, `url`, `Tipo_Especialidad_idTipo_Especialidad`) VALUES (2, 'Nicthe', 'Castellanos', '65821990', 'nicthe.rodas@gmail.com', '123546578', 1, NULL, 1);
INSERT INTO `clinica_dental`.`dentista` (`idDentista`, `nombre`, `apellido`, `numero_telefono`, `correo_electronico`, `no_colegiado`, `estado`, `url`, `Tipo_Especialidad_idTipo_Especialidad`) VALUES (3, 'Concepcion', 'Rodriguez', '23432432', 'concepcion.rodriguez@gmail.com', '34467657', 1, NULL, 3);
INSERT INTO `clinica_dental`.`dentista` (`idDentista`, `nombre`, `apellido`, `numero_telefono`, `correo_electronico`, `no_colegiado`, `estado`, `url`, `Tipo_Especialidad_idTipo_Especialidad`) VALUES (4, 'Saul', 'Perez', '44535345', 'saul.perez@gmail.com', '54623413', 1, NULL, 4);
INSERT INTO `clinica_dental`.`dentista` (`idDentista`, `nombre`, `apellido`, `numero_telefono`, `correo_electronico`, `no_colegiado`, `estado`, `url`, `Tipo_Especialidad_idTipo_Especialidad`) VALUES (5, 'Paco', 'Hernandez', '23423423', 'paco.hernandez@gmail.com', '778689098', 1, NULL, 5);

COMMIT;


-- -----------------------------------------------------
-- Data for table `clinica_dental`.`tipo_usuario`
-- -----------------------------------------------------
START TRANSACTION;
USE `clinica_dental`;
INSERT INTO `clinica_dental`.`tipo_usuario` (`idTipo_Usuario`, `descripcion`, `permisos`) VALUES (1, 'Dentista', 'inventario, ventas, recursos, financiero');
INSERT INTO `clinica_dental`.`tipo_usuario` (`idTipo_Usuario`, `descripcion`, `permisos`) VALUES (2, 'Asistente', 'inventario, ventas');

COMMIT;