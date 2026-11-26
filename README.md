# Costa Rica: la legislación en git

[English](README.en.md)

La legislación de Costa Rica como historia de git: un archivo por artículo, un commit por versión fechado el día en que entró en vigor (12:00, hora de Costa Rica), y como autor de cada commit la norma que hizo el cambio. `git blame` nombra la ley detrás de cada línea; `git log` lista cada cambio de un artículo; una fecha da el texto vigente ese día.

Forma parte de [lexifina/global-law](https://github.com/lexifina/global-law), que lee este repositorio como `cr/national/acts`.

**Qué contiene ahora:** la Constitución Política de 1949 y los códigos vigentes (Civil, Penal, Trabajo, Comercio, Procesal Civil, Procesal Penal, Familia, Normas y Procedimientos Tributarios, Municipal, Electoral, Niñez y Adolescencia y otros), con todas las versiones que guarda SINALEVI. Las Leyes y los Tratados Internacionales se añaden a medida que se descargan. Ver [PLAN.md](PLAN.md).

Los textos están en español, tal como los publica SINALEVI.

## Estructura

| Carpeta | Contenido | Ejemplo |
| --- | --- | --- |
| `constitucion/` | Constitución Política de 1949, cada versión; las constituciones históricas, cada una en su carpeta | `constitucion/1949/articulo-48.md` |
| `codigos/` | los códigos vigentes, cada versión | `codigos/codigo-penal/articulo-111.md` (Ley N° 4573) |
| `leyes/` | las demás Leyes; los números anteriores a 1922 se repiten, y entonces llevan el año | `leyes/8968/articulo-5.md`, `leyes/63-1887/` |
| `tratados/` | Tratados Internacionales, por año | `tratados/1970/<nombre>/` |

Cada norma tiene un `README.md` con su ficha de SINALEVI y la tabla de versiones, e `index.txt` con el orden de los artículos.

## Commits

- Fecha: 12:00 America/Costa_Rica del día de entrada en vigor (fechas anteriores a 1970: 1970-01-01, la fecha real en el trailer `In-force:`).
- Autor: la norma que hizo el cambio (`ley-<n>@sinalevi.invalid`); si SINALEVI reúne varias normas en una versión, el autor es SINALEVI y las normas van en trailers `Candidate:` o `Consolidates:`.
- Trailers: `In-force:`, `In-force-evidence:`, `Enacted:`, `Published:`, `Gazette:`, `Affecting:`, `Version:`, `Source:`.
- Los cambios con vigencia futura van en la rama `future`.

## Fuente

| Fuente | Qué | Versiones |
| --- | --- | --- |
| [SINALEVI](https://sinalevi.go.cr) (Sistema Nacional de Legislación Vigente, Procuraduría General de la República) | texto completo de cada norma | sí: versiones numeradas de cada norma, cada una con su texto y las normas que la afectaron |

## Licencia

Ver [`LICENSE`](LICENSE). El trabajo de Lexifina (estructura, documentación, herramientas, textos de los commits) es CC0 1.0. Ninguna IA escribió texto legal.
