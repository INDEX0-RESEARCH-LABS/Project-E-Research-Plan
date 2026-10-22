# Project E — Source Verification Table

**Verification date:** 2026-10-23  
**Method:** Crossref `api.crossref.org/works/<doi>` for DOI records; DOI resolver for redirects; direct HTTP retrieval for institutional pages/PDFs.  
**Rule:** A source is "verified" only when the identifier resolves and the title/year/venue or page text matches the claim it is used for. A verified source does not validate every number in it; the specific claim must still be page-checked in Gate 1.

The existing repository registry (`research/source_registry.csv`) is marked "abstracts only." This table does not upgrade those records to full-text review.

---

## 1. Existing registry (all 12 verified through Crossref)

| ID | Citation | DOI | Verified record | Claim it can support | Limits |
|---|---|---|---|---|---|
| S01 | LaPotin et al., "Thermophotovoltaic efficiency of 40%," *Nature* 604, 287–291 (2022) | 10.1038/s41586-022-04473-y | Title/year/venue match | TPV cell efficiency >40% at 1900–2400 °C | Cell-level result; not a system; not a portable heat source |
| S02 | Snyder & Toberer, "Complex thermoelectric materials," *Nature Materials* 7, 105–114 (2008) | 10.1038/nmat2090 | Match | ZT physics and TEG efficiency ceiling | Review; not a device quote |
| S03 | Simon & Gogotsi, "Materials for electrochemical capacitors," *Nature Materials* 7, 845–854 (2008) | 10.1038/nmat2297 | Match | Supercapacitor energy/power split | Review; older material set |
| S04 | Nitta et al., "Li-ion battery materials: present and future," *Materials Today* 18, 252–264 (2015) | 10.1016/j.mattod.2014.10.040 | Match | Li-ion energy density and materials limits | Review; not a pack datasheet |
| S05 | Shockley & Queisser, "Detailed balance limit of efficiency of p-n junction solar cells," *J. Appl. Phys.* 32, 510 (1961) | 10.1063/1.1736034 | Match | Single-junction thermodynamic ceiling | Ideal limit; not practical module efficiency |
| S06 | Dunn, Kamath & Tarascon, "Electrical energy storage for the grid: a battery of choices," *Science* 334, 928–935 (2011) | 10.1126/science.1212741 | Match | Grid storage comparison and round-trip context | Review; not portable |
| S07 | Champier, "Thermoelectric generators: a review of applications," *Energy Conversion and Management* 140, 167–181 (2017) | 10.1016/j.enconman.2017.02.070 | Match | Real TEG system efficiencies | Review; application-dependent |
| S08 | Benato & Stoppato, "Pumped thermal electricity storage: a technology overview," *Thermal Science and Engineering Progress* 6, 1–17 (2018) | 10.1016/j.tsep.2018.01.017 | Match | Thermal-mechanical storage efficiency/cost drivers | Review; grid scale |
| S09 | Sharma et al., "Review on thermal energy storage with phase change materials and applications," *Renewable and Sustainable Energy Reviews* 13, 318–345 (2009) | 10.1016/j.rser.2007.10.005 | Match | Latent-heat storage density and heat-transfer limits | Review; materials, not system |
| S10 | Luo et al., "Overview of current development in electrical energy storage technologies...," *Applied Energy* 137, 511–536 (2015) | 10.1016/j.apenergy.2014.09.081 | Match | Cross-technology efficiency/lifetime/cost | Review; dates quickly |
| S11 | Winter, "Hydrogen and fuel cells: towards a sustainable energy future," *Energy Policy* 36, 4356–4362 (2008) | 10.1016/j.enpol.2008.09.036 | Match | Hydrogen/fuel-cell efficiency chain and infrastructure | Perspective; older costs |
| S12 | Hung, Shai & Wang, "A review of organic Rankine cycles (ORCs) for the recovery of low-grade waste heat," *Energy* 22, 661–667 (1997) | 10.1016/s0360-5442(96)00165-x | Match | Low-grade heat-engine efficiency | Older; small/medium systems |

---

## 2. New sources verified for the initial landscape

| ID | Citation | DOI / URL | Verification | Claim it can support | Limits |
|---|---|---|---|---|---|
| N01 | Schmuch et al., "Performance and cost of materials for lithium-based rechargeable automotive batteries," *Nature Energy* 3, 267–278 (2018) | 10.1038/s41560-018-0107-2 | Crossref record; title/year/venue match | Li-ion cell materials, energy density, and cost trajectory | Automotive focus; not a pack quote |
| N02 | Janek & Zeier, "A solid future for battery development," *Nature Energy* 1, 16141 (2016) | 10.1038/nenergy.2016.141 | Crossref match | Solid-state battery promise and interface/processing barriers | Perspective; not commercial status |
| N03 | Staffell et al., "The role of hydrogen and fuel cells in the global energy system," *Energy & Environmental Science* 12, 463–491 (2019) | 10.1039/C8EE01157E | Crossref match; abstract retrieved | Hydrogen/fuel-cell system role and infrastructure context | Review; not a 50% stack quote |
| N04 | Eberle, Felderhoff & Schüth, "Chemical and physical solutions for hydrogen storage," *Angew. Chem. Int. Ed.* 48, 6608–6630 (2009) | 10.1002/anie.200806293 | Crossref match; abstract retrieved | High-pressure, cryogenic, adsorptive, and hydride storage tradeoffs | Review; older system data |
| N05 | Amiryar & Pullen, "A review of flywheel energy storage system technologies and their applications," *Applied Sciences* 7, 286 (2017) | 10.3390/app7030286 | Crossref match; abstract retrieved | Flywheel high power, long life, MJ-level storage; containment/safety | Review; not a 10 kWh product |
| N06 | Budt et al., "A review on compressed air energy storage: basic principles, past milestones and recent developments," *Applied Energy* 170, 250–268 (2016) | 10.1016/j.apenergy.2016.02.108 | Crossref match | CAES principles, bulk storage, efficiency drivers | Grid-scale; not portable |
| N07 | Rehman, Al-Hadhrami & Alam, "Pumped hydro energy storage system: a technological review," *Renewable and Sustainable Energy Reviews* 44, 586–598 (2015) | 10.1016/j.rser.2014.12.040 | Crossref match | Pumped-hydro technology, siting, scale | Grid-scale; not portable |
| N08 | Gibson et al., "The Kilopower Reactor Using Stirling TechnologY (KRUSTY) nuclear ground test results and lessons learned," AIAA 2018-4973 (2018) | 10.2514/6.2018-4973 | Crossref match; OpenAlex abstract retrieved | 1 kWe fission–Stirling ground test; 10 kWe is a design concept; reactor dynamics and failure tolerance | Space reactor; not a product; shielding/regulatory mass not included |
| N09 | National Academies of Sciences, Engineering, and Medicine, *Bringing Fusion to the U.S. Grid* (2021) | 10.17226/25991 | DOI resolves to National Academies publication page | Fusion pilot-plant roadmap; tritium, neutron, and facility constraints | Consensus study; not a compact-core design |
| N10 | Fraunhofer ISE, *Photovoltaics Report* (Freiburg, 14 July 2026) | https://www.ise.fraunhofer.de/content/dam/ise/de/documents/publications/studies/Photovoltaics-Report.pdf | PDF retrieved; text: commercial Si modules "just under 25%" | Practical commercial module efficiency around 25% in 2026 | Report; system efficiency lower; location-dependent |
| N11 | U.S. Department of Energy, "Hydrogen Storage" (Office of Energy Efficiency and Renewable Energy) | https://www.energy.gov/eere/fuelcells/hydrogen-storage | HTTP 200; text: gas storage typically 350–700 bar (5,000–10,000 psi) | Physical H2 storage pressure regime and density penalty | Program page; not a tank datasheet |
| N12 | U.S. Department of Energy, *Report of the Review of Low Energy Nuclear Reactions* (2004) | https://www.lenr-canr.org/acrobat/DOEreportofth.pdf | PDF retrieved; review text: occurrence "not conclusively demonstrated" | Negative screen for LENR/cold-fusion claims | Archival copy; confirm official DOE provenance in Gate 1 |
| N13 | NASA, "Kilopower Reactor Using Stirling TechnologY (KRUSTY)" technical report | https://ntrs.nasa.gov/api/citations/20180007389/downloads/20180007389.pdf | PDF retrieved; text: 1 kWe test with half engines/heat pipes failed; 10 kWe design context | Kilopower test scope and scale | NASA TM; not an independent replication |
| N14 | NASA, "Kilopower reactor development and the path to higher power missions" | https://ntrs.nasa.gov/api/citations/20170011067/downloads/20170011067.pdf | PDF retrieved; 10-kWe system and mission mass trade context | 10-kWe system scale and mission integration | Pre-test study; not a flight product |

---

## 3. Sources explicitly **not** verified / not used

- NREL cell-efficiency and module-efficiency pages: repeated transport failures from this environment. Replaced by Fraunhofer ISE N10 for the practical module claim.
- NASA `nasa.gov/feature/kilopower/`: returned 404. Replaced by NTRS N13/N14.
- IAEA SMR topic page: HTTP 403 from this environment. SMR/regulatory claims are marked pending.
- Manufacturer datasheets for diesel gensets, LFP packs, PEM stacks, and 700 bar tanks: not retrieved. All such values remain E0/E1 until quotations or datasheets are archived.
- Any patent: not treated as evidence of feasibility.
- Any LENR/over-unity/zero-point claim: not accepted; N12 is used only as a negative review.

---

## 4. Citation rules for the discovery program

1. Every quantitative claim gets a source ID and a page/figure/table locator.
2. E2 requires a DOI/datasheet in the registry; otherwise the value is E1.
3. Reviews support context, not a specific device performance number.
4. A patent is prior art, not proof.
5. A simulation is not a measurement; a measurement is not field qualification.
6. Negative results are recorded with the same care as positive ones.
