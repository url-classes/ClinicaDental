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
CREATE SCHEMA IF NOT EXISTS `clinica_dental` ;
USE `clinica_dental` ;

-- -----------------------------------------------------
-- Table `clinica_dental`.`alergia`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `clinica_dental`.`alergia` (
  `idAlergia` INT(11) NOT NULL AUTO_INCREMENT,
  `descripcion` VARCHAR(45) NULL DEFAULT NULL,
  PRIMARY KEY (`idAlergia`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `clinica_dental`.`cita`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `clinica_dental`.`cita` (
  `idCita` INT(11) NOT NULL AUTO_INCREMENT,
  `fecha_propuesta` DATETIME NULL DEFAULT NULL,
  PRIMARY KEY (`idCita`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `clinica_dental`.`paciente`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `clinica_dental`.`paciente` (
  `idPaciente` INT(11) NOT NULL AUTO_INCREMENT,
  `nombre` VARCHAR(45) NULL DEFAULT NULL,
  `apellido` VARCHAR(45) NULL DEFAULT NULL,
  `numero_telefonico` VARCHAR(45) NULL DEFAULT NULL,
  `edad` INT(11) NULL DEFAULT NULL,
  `numero_seguro` VARCHAR(45) NULL DEFAULT NULL,
  `Cita_idCita` INT(11) NOT NULL,
  PRIMARY KEY (`idPaciente`),
  INDEX `fk_Paciente_Cita1_idx` (`Cita_idCita` ASC) VISIBLE,
  CONSTRAINT `fk_Paciente_Cita1`
    FOREIGN KEY (`Cita_idCita`)
    REFERENCES `clinica_dental`.`cita` (`idCita`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


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
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `clinica_dental`.`asistente`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `clinica_dental`.`asistente` (
  `idAsistente` INT(11) NOT NULL AUTO_INCREMENT,
  `nombre` VARCHAR(45) NULL DEFAULT NULL,
  `apellido` VARCHAR(45) NULL DEFAULT NULL,
  `escolaridad` VARCHAR(45) NULL DEFAULT NULL,
  `salario` FLOAT NULL DEFAULT NULL,
  PRIMARY KEY (`idAsistente`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `clinica_dental`.`tipo_especialidad`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `clinica_dental`.`tipo_especialidad` (
  `idTipo_Especialidad` INT(11) NOT NULL AUTO_INCREMENT,
  `descripcion` VARCHAR(45) NULL DEFAULT NULL,
  PRIMARY KEY (`idTipo_Especialidad`))
ENGINE = InnoDB;


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
  `Tipo_Especialidad_idTipo_Especialidad` INT(11) NOT NULL,
  PRIMARY KEY (`idDentista`),
  INDEX `fk_Dentista_Tipo_Especialidad1_idx` (`Tipo_Especialidad_idTipo_Especialidad` ASC) VISIBLE,
  CONSTRAINT `fk_Dentista_Tipo_Especialidad1`
    FOREIGN KEY (`Tipo_Especialidad_idTipo_Especialidad`)
    REFERENCES `clinica_dental`.`tipo_especialidad` (`idTipo_Especialidad`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `clinica_dental`.`tratamiento`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `clinica_dental`.`tratamiento` (
  `idTratamientno` INT(11) NOT NULL AUTO_INCREMENT,
  `detalle` VARCHAR(45) NULL DEFAULT NULL,
  `precio` FLOAT NULL DEFAULT NULL,
  `cantidad_citas` INT(11) NULL DEFAULT NULL,
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
ENGINE = InnoDB;


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
ENGINE = InnoDB;


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
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `clinica_dental`.`material`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `clinica_dental`.`material` (
  `idMaterial` INT(11) NOT NULL AUTO_INCREMENT,
  `descripcion` VARCHAR(45) NULL DEFAULT NULL,
  `serie_modelo` VARCHAR(45) NULL DEFAULT NULL,
  `cantidad` INT(11) NULL DEFAULT NULL,
  `precio_individual` FLOAT NULL DEFAULT NULL,
  PRIMARY KEY (`idMaterial`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `clinica_dental`.`tipo_usuario`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `clinica_dental`.`tipo_usuario` (
  `idTipo_Usuario` INT(11) NOT NULL AUTO_INCREMENT,
  `descripcion` VARCHAR(45) NULL DEFAULT NULL,
  `permisos` VARCHAR(45) NULL DEFAULT NULL,
  PRIMARY KEY (`idTipo_Usuario`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `clinica_dental`.`tratamiento_material`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `clinica_dental`.`tratamiento_material` (
  `Tratamiento_idTratamientno` INT(11) NOT NULL,
  `Material_idMaterial` INT(11) NOT NULL,
  `cantidad_utilizada` INT NULL,
  PRIMARY KEY (`Tratamiento_idTratamientno`, `Material_idMaterial`),
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
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `clinica_dental`.`usuario`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `clinica_dental`.`usuario` (
  `idUsuario` INT(11) NOT NULL AUTO_INCREMENT,
  `nombre_usuario` VARCHAR(45) NOT NULL,
  `password` VARCHAR(255) NULL DEFAULT NULL,
  `last_login` DATETIME NULL,
  `Dentista_idDentista` INT(11) NULL,
  `Tipo_Usuario_idTipo_Usuario` INT(11) NOT NULL,
  `Asistente_idAsistente` INT(11) NULL,
  PRIMARY KEY (`idUsuario`),
  INDEX `fk_Usuario_Dentista1_idx` (`Dentista_idDentista` ASC) VISIBLE,
  INDEX `fk_Usuario_Tipo_Usuario1_idx` (`Tipo_Usuario_idTipo_Usuario` ASC) VISIBLE,
  INDEX `fk_Usuario_Asistente1_idx` (`Asistente_idAsistente` ASC) VISIBLE,
  CONSTRAINT `fk_Usuario_Dentista1`
    FOREIGN KEY (`Dentista_idDentista`)
    REFERENCES `clinica_dental`.`dentista` (`idDentista`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Usuario_Tipo_Usuario1`
    FOREIGN KEY (`Tipo_Usuario_idTipo_Usuario`)
    REFERENCES `clinica_dental`.`tipo_usuario` (`idTipo_Usuario`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Usuario_Asistente1`
    FOREIGN KEY (`Asistente_idAsistente`)
    REFERENCES `clinica_dental`.`asistente` (`idAsistente`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
