-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema clinica_dental
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema clinica_dental
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `clinica_dental` DEFAULT CHARACTER SET utf8 ;
USE `clinica_dental` ;

-- -----------------------------------------------------
-- Table `clinica_dental`.`Tipo_Usuario`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `clinica_dental`.`Tipo_Usuario` (
  `idTipo_Usuario` INT NOT NULL,
  `descripcion` VARCHAR(45) NULL,
  `permisos` VARCHAR(45) NULL,
  PRIMARY KEY (`idTipo_Usuario`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `clinica_dental`.`Tipo_Especialidad`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `clinica_dental`.`Tipo_Especialidad` (
  `idTipo_Especialidad` INT NOT NULL,
  `descripcion` VARCHAR(45) NULL,
  PRIMARY KEY (`idTipo_Especialidad`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `clinica_dental`.`Dentista`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `clinica_dental`.`Dentista` (
  `idDentista` INT NOT NULL,
  `nombre` VARCHAR(45) NULL,
  `apellido` VARCHAR(45) NULL,
  `numero_telefono` VARCHAR(45) NULL,
  `correo_electronico` VARCHAR(45) NULL,
  `no_colegiado` VARCHAR(45) NULL,
  `Tipo_Especialidad_idTipo_Especialidad` INT NOT NULL,
  PRIMARY KEY (`idDentista`),
  INDEX `fk_Dentista_Tipo_Especialidad1_idx` (`Tipo_Especialidad_idTipo_Especialidad` ASC) VISIBLE,
  CONSTRAINT `fk_Dentista_Tipo_Especialidad1`
    FOREIGN KEY (`Tipo_Especialidad_idTipo_Especialidad`)
    REFERENCES `clinica_dental`.`Tipo_Especialidad` (`idTipo_Especialidad`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `clinica_dental`.`Usuario`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `clinica_dental`.`Usuario` (
  `idUsuario` INT NOT NULL,
  `nombre_usuario` VARCHAR(45) NULL,
  `password` VARCHAR(45) NULL,
  `Dentista_idDentista` INT NOT NULL,
  `Tipo_Usuario_idTipo_Usuario` INT NOT NULL,
  PRIMARY KEY (`idUsuario`),
  INDEX `fk_Usuario_Dentista1_idx` (`Dentista_idDentista` ASC) VISIBLE,
  INDEX `fk_Usuario_Tipo_Usuario1_idx` (`Tipo_Usuario_idTipo_Usuario` ASC) VISIBLE,
  CONSTRAINT `fk_Usuario_Dentista1`
    FOREIGN KEY (`Dentista_idDentista`)
    REFERENCES `clinica_dental`.`Dentista` (`idDentista`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Usuario_Tipo_Usuario1`
    FOREIGN KEY (`Tipo_Usuario_idTipo_Usuario`)
    REFERENCES `clinica_dental`.`Tipo_Usuario` (`idTipo_Usuario`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `clinica_dental`.`Asistente`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `clinica_dental`.`Asistente` (
  `idAsistente` INT NOT NULL,
  `nombre` VARCHAR(45) NULL,
  `apellido` VARCHAR(45) NULL,
  `escolaridad` VARCHAR(45) NULL,
  `salario` FLOAT NULL,
  `Usuario_idUsuario` INT NOT NULL,
  PRIMARY KEY (`idAsistente`),
  INDEX `fk_Asistente_Usuario1_idx` (`Usuario_idUsuario` ASC) VISIBLE,
  CONSTRAINT `fk_Asistente_Usuario1`
    FOREIGN KEY (`Usuario_idUsuario`)
    REFERENCES `clinica_dental`.`Usuario` (`idUsuario`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `clinica_dental`.`Cita`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `clinica_dental`.`Cita` (
  `idCita` INT NOT NULL,
  `fecha_propuesta` DATETIME NULL,
  PRIMARY KEY (`idCita`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `clinica_dental`.`Tratamiento`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `clinica_dental`.`Tratamiento` (
  `idTratamientno` INT NOT NULL,
  `detalle` VARCHAR(45) NULL,
  `precio` FLOAT NULL,
  `cantidad_citas` INT NULL,
  `Cita_idCita` INT NOT NULL,
  `Asistente_idAsistente` INT NOT NULL,
  PRIMARY KEY (`idTratamientno`),
  INDEX `fk_Tratamiento_Cita1_idx` (`Cita_idCita` ASC) VISIBLE,
  INDEX `fk_Tratamiento_Asistente1_idx` (`Asistente_idAsistente` ASC) VISIBLE,
  CONSTRAINT `fk_Tratamiento_Cita1`
    FOREIGN KEY (`Cita_idCita`)
    REFERENCES `clinica_dental`.`Cita` (`idCita`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Tratamiento_Asistente1`
    FOREIGN KEY (`Asistente_idAsistente`)
    REFERENCES `clinica_dental`.`Asistente` (`idAsistente`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `clinica_dental`.`Material`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `clinica_dental`.`Material` (
  `idMaterial` INT NOT NULL,
  `descripcion` VARCHAR(45) NULL,
  `serie_modelo` VARCHAR(45) NULL,
  `cantidad` INT NULL,
  `precio_individual` FLOAT NULL,
  PRIMARY KEY (`idMaterial`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `clinica_dental`.`Paciente`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `clinica_dental`.`Paciente` (
  `idPaciente` INT NOT NULL,
  `nombre` VARCHAR(45) NULL,
  `apellido` VARCHAR(45) NULL,
  `numero_telefonico` VARCHAR(45) NULL,
  `edad` INT NULL,
  `numero_seguro` VARCHAR(45) NULL,
  `Cita_idCita` INT NOT NULL,
  PRIMARY KEY (`idPaciente`),
  INDEX `fk_Paciente_Cita1_idx` (`Cita_idCita` ASC) VISIBLE,
  CONSTRAINT `fk_Paciente_Cita1`
    FOREIGN KEY (`Cita_idCita`)
    REFERENCES `clinica_dental`.`Cita` (`idCita`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `clinica_dental`.`Alergia`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `clinica_dental`.`Alergia` (
  `idAlergia` INT NOT NULL,
  `descripcion` VARCHAR(45) NULL,
  PRIMARY KEY (`idAlergia`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `clinica_dental`.`Factura`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `clinica_dental`.`Factura` (
  `idFactura` INT NOT NULL,
  `detalle` VARCHAR(45) NULL,
  `cantidad_servicios` INT NULL,
  `fecha` DATETIME NULL,
  `total` FLOAT NULL,
  `Tratamiento_idTratamientno` INT NOT NULL,
  PRIMARY KEY (`idFactura`),
  INDEX `fk_Factura_Tratamiento1_idx` (`Tratamiento_idTratamientno` ASC) VISIBLE,
  CONSTRAINT `fk_Factura_Tratamiento1`
    FOREIGN KEY (`Tratamiento_idTratamientno`)
    REFERENCES `clinica_dental`.`Tratamiento` (`idTratamientno`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `clinica_dental`.`Dentista_has_Tratamiento`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `clinica_dental`.`Dentista_has_Tratamiento` (
  `Dentista_idDentista` INT NOT NULL,
  `Tratamiento_idTratamientno` INT NOT NULL,
  PRIMARY KEY (`Dentista_idDentista`, `Tratamiento_idTratamientno`),
  INDEX `fk_Dentista_has_Tratamiento_Tratamiento1_idx` (`Tratamiento_idTratamientno` ASC) VISIBLE,
  INDEX `fk_Dentista_has_Tratamiento_Dentista1_idx` (`Dentista_idDentista` ASC) VISIBLE,
  CONSTRAINT `fk_Dentista_has_Tratamiento_Dentista1`
    FOREIGN KEY (`Dentista_idDentista`)
    REFERENCES `clinica_dental`.`Dentista` (`idDentista`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Dentista_has_Tratamiento_Tratamiento1`
    FOREIGN KEY (`Tratamiento_idTratamientno`)
    REFERENCES `clinica_dental`.`Tratamiento` (`idTratamientno`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `clinica_dental`.`Alergia_has_Paciente`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `clinica_dental`.`Alergia_has_Paciente` (
  `Alergia_idAlergia` INT NOT NULL,
  `Paciente_idPaciente` INT NOT NULL,
  PRIMARY KEY (`Alergia_idAlergia`, `Paciente_idPaciente`),
  INDEX `fk_Alergia_has_Paciente_Paciente1_idx` (`Paciente_idPaciente` ASC) VISIBLE,
  INDEX `fk_Alergia_has_Paciente_Alergia1_idx` (`Alergia_idAlergia` ASC) VISIBLE,
  CONSTRAINT `fk_Alergia_has_Paciente_Alergia1`
    FOREIGN KEY (`Alergia_idAlergia`)
    REFERENCES `clinica_dental`.`Alergia` (`idAlergia`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Alergia_has_Paciente_Paciente1`
    FOREIGN KEY (`Paciente_idPaciente`)
    REFERENCES `clinica_dental`.`Paciente` (`idPaciente`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `clinica_dental`.`Tratamiento_has_Material`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `clinica_dental`.`Tratamiento_has_Material` (
  `Tratamiento_idTratamientno` INT NOT NULL,
  `Material_idMaterial` INT NOT NULL,
  PRIMARY KEY (`Tratamiento_idTratamientno`, `Material_idMaterial`),
  INDEX `fk_Tratamiento_has_Material_Material1_idx` (`Material_idMaterial` ASC) VISIBLE,
  INDEX `fk_Tratamiento_has_Material_Tratamiento1_idx` (`Tratamiento_idTratamientno` ASC) VISIBLE,
  CONSTRAINT `fk_Tratamiento_has_Material_Tratamiento1`
    FOREIGN KEY (`Tratamiento_idTratamientno`)
    REFERENCES `clinica_dental`.`Tratamiento` (`idTratamientno`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Tratamiento_has_Material_Material1`
    FOREIGN KEY (`Material_idMaterial`)
    REFERENCES `clinica_dental`.`Material` (`idMaterial`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
