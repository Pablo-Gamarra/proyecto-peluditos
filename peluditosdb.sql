-- phpMyAdmin SQL Dump
-- version 4.1.14
-- http://www.phpmyadmin.net
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 30-04-2020 a las 20:19:57
-- Versión del servidor: 5.6.17
-- Versión de PHP: 5.5.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;

--
-- Base de datos: `peluditosdb`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `mascotas`
--

CREATE TABLE IF NOT EXISTS `mascotas` (
  `id` int(255) NOT NULL AUTO_INCREMENT,
  `estado` varchar(255) COLLATE utf8_spanish_ci NOT NULL,
  `departamento` varchar(255) COLLATE utf8_spanish_ci NOT NULL,
  `ciudad` varchar(255) COLLATE utf8_spanish_ci NOT NULL,
  `especie` varchar(255) COLLATE utf8_spanish_ci NOT NULL,
  `nombre` varchar(255) COLLATE utf8_spanish_ci NOT NULL,
  `tamaño` varchar(255) COLLATE utf8_spanish_ci NOT NULL,
  `peso` varchar(255) COLLATE utf8_spanish_ci NOT NULL,
  `color` varchar(255) COLLATE utf8_spanish_ci NOT NULL,
  `email` varchar(255) COLLATE utf8_spanish_ci NOT NULL,
  `telefono` varchar(255) COLLATE utf8_spanish_ci NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 COLLATE=utf8_spanish_ci AUTO_INCREMENT=16 ;

--
-- Volcado de datos para la tabla `mascotas`
--

INSERT INTO `mascotas` (`id`, `estado`, `departamento`, `ciudad`, `especie`, `nombre`, `tamaño`, `peso`, `color`, `email`, `telefono`) VALUES
(4, 'Adopción', 'Canelones', 'Santa Lucia', 'Perro', 'Blacky', 'Grande', '30Kgs', 'Gris', 'blacky@gmail.com', '092999555'),
(5, 'Encontrado', 'Canelones', 'Las Piedras', 'Perro', 'Firulais', 'Mediano', '15Kgs', 'Marron y blanco', 'firulais@hotmail.com', '098987878'),
(7, 'Adopción', 'Canelones', 'La Paz', 'Perro', 'Fido', 'Pequeño', '10Kgs', 'Gris', 'fido@hotmail.com', '093256456'),
(8, 'Adopción', 'Canelones', 'Juanico', 'Gato', 'Miyu', 'Pequeño', '10Kgs', 'Gris y blanco', 'miyu@hotmail.com', '097456123'),
(14, 'Adopción', 'Canelones', 'Canelones', 'Perro', 'Chiquitua', 'Pequeño', '10Kgs', 'Negro y marron', 'chiqui@gmail.com', '097123123'),
(15, 'Encontrado', 'Canelones', 'San Jacinto', 'Perro', 'Pipo', 'Grande', '5Kgs', 'Marron', 'pipo2019@gmail.com', '093565656');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `tiendas`
--

CREATE TABLE IF NOT EXISTS `tiendas` (
  `id` int(255) NOT NULL AUTO_INCREMENT,
  `departamento` varchar(255) COLLATE utf8_spanish_ci NOT NULL,
  `ciudad` varchar(255) COLLATE utf8_spanish_ci NOT NULL,
  `nombre` varchar(255) COLLATE utf8_spanish_ci NOT NULL,
  `horario` varchar(255) COLLATE utf8_spanish_ci NOT NULL,
  `direccion` varchar(255) COLLATE utf8_spanish_ci NOT NULL,
  `telefono` varchar(255) COLLATE utf8_spanish_ci NOT NULL,
  `email` varchar(255) COLLATE utf8_spanish_ci NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_spanish_ci AUTO_INCREMENT=1 ;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `usuarios`
--

CREATE TABLE IF NOT EXISTS `usuarios` (
  `id` int(255) NOT NULL AUTO_INCREMENT,
  `nombre` varchar(255) COLLATE utf8_spanish_ci NOT NULL,
  `email` varchar(255) COLLATE utf8_spanish_ci NOT NULL,
  `contraseña` varchar(255) COLLATE utf8_spanish_ci NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 COLLATE=utf8_spanish_ci AUTO_INCREMENT=9 ;

--
-- Volcado de datos para la tabla `usuarios`
--

INSERT INTO `usuarios` (`id`, `nombre`, `email`, `contraseña`) VALUES
(7, 'Viviana', 'vivi156@gmail.com', '$2b$12$fcnOrv7f52Tyx7bq4RAoCOomCQbhdQ9QOU84kCkJ8sbj5HGkJUM3C'),
(8, 'Pablo', 'pablo127@gmail.com', '$2b$12$Z/lz33uau0NwZlIsfrOurusun3.3aVAVW3e/xxxU96iMRgvF2F9ji');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `veterinarias`
--

CREATE TABLE IF NOT EXISTS `veterinarias` (
  `id` int(255) NOT NULL AUTO_INCREMENT,
  `departamento` varchar(255) COLLATE utf8_spanish_ci NOT NULL,
  `ciudad` varchar(255) COLLATE utf8_spanish_ci NOT NULL,
  `nombre` varchar(255) COLLATE utf8_spanish_ci NOT NULL,
  `horario` varchar(255) COLLATE utf8_spanish_ci NOT NULL,
  `direccion` varchar(255) COLLATE utf8_spanish_ci NOT NULL,
  `telefono` varchar(255) COLLATE utf8_spanish_ci NOT NULL,
  `email` varchar(255) COLLATE utf8_spanish_ci NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 COLLATE=utf8_spanish_ci AUTO_INCREMENT=5 ;

--
-- Volcado de datos para la tabla `veterinarias`
--

INSERT INTO `veterinarias` (`id`, `departamento`, `ciudad`, `nombre`, `horario`, `direccion`, `telefono`, `email`) VALUES
(1, 'Canelones', 'San Jacinto', 'Veterinaria Jacinto', 'LaV - 9a12 14a18', 'Rodo 289', '4336 7689', 'jacintoveterinaria@gmail.com'),
(2, 'Canelones', 'Santa Lucia', 'Veterinaria Merida', 'LaV 9a12 - 14a18', 'Rivera 456', '43348912', 'merida@gmail.com'),
(3, 'Canelones', 'Canelones', 'Veterinaria Pompita', 'LaV 9 a 18', 'Herrera 264', '4332 5614', 'pompita20@hotmail.com'),
(4, 'Canelones', 'Santa Lucia', 'Veterinaria VEC', 'LaV 8 a 18', 'Rivera 268', '43345656', 'vecveterinaria20@gmail.com');

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
