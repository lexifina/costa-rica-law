ANEXO 2. Glosario de fórmulas.
Fórmula No. | Descripción | Detalle de la fórmula
1 | Precio de venta al consumidor final por litro, para el combustible "i" en el ajuste tarifario "t". | mf PCDFLi,t = PPCVi,t + ∑ MGLi,t,m m=mp
2 | Precio de venta al consumidor final por kilogramo, para el combustible "i" en el ajuste tarifario "t". | mf PCDFKi,t = PPCMi,t + ∑ MGKi,t,m m=mp
3 | Margen de suministro en el segmento "m" de la cadena, para el combustible "i", expresado en colones por kilogramo, en el ajuste tarifario "t". | 1000 MGKi,t,m = MGLi,t,m ∗ DRF i,t
4 | Precio de venta en terminales de ventas, del combustible "i" que se comercializa en volumen, en el ajuste tarifario "t" | PPCVi,t = COAi,t + ASi,t − SEi,t − SCi,t + DAi,t − ALEi,t + IU + CAi,t + MOi,t + RSBTi,t − ALOi,t
[imagen]
Fórmula No. | Descripción | Detalle de la fórmula
5 | Precio de venta en terminales de ventas, del combustible "i" que se comercializa en masa, en el ajuste tarifario "t". | PPCMi,t = (COAi,t + ASi,t − SEi,t − SCi,t + DAi,t − ALEi,t + IUi,t + CAi,t + MOi,t + RSBTi,t − ALOi,t ) 1000 ∗ DRFi,t
6 | Densidad de referencia del combustible "i", en el ajuste tarifario "t". | H DRFi,t = ∑ γh ∗ DRFh,t h=1
7 | Precio máximo en colones por litro, en terminales de ventas, de los combustibles Jet fuel A-1, Av-gas e IFO 380, que se vende en aeropuertos o puertos, del combustible "i" para el ajuste tarifario "t". | NPPCmáxȻi,t = COAi,t + σi,t + ASi,t − SEi,t − SCi,t + DAi,t − ALEi,t + IUi,t + CAi,t + MOi,t + RSBTi,t − ALOi,t
8 | Precio mínimo en colones por litro, en terminales de ventas, de los combustibles Jet fuel A- 1, Av-gas e IFO 380, que se vende en aeropuertos o puertos, del combustible "i" para el ajuste tarifario "t". | NPPCminȻi,t = COAi,t − σi,t + ASi,t − SEi,t − SCi,t + DAi,t − ALEi,t + IUi,t + CAi,t + MOi,t + RSBTi,t − ALOi,t
9 | Costo de adquisición por litro del combustible "i" en el ajuste tarifario "t". | COA = C OA Bi,t i,t FCi
| Costo de adquisición en colones por barril del |
[imagen]
[imagen]
[imagen]
Fórmula No. | Descripción | Detalle de la fórmula
10 | combustible "i", que incluye: precio del producto (primas o descuentos incorporados), flete de transporte internacional, seguro de transporte internacional, el margen de comercialización del proveedor (trader) y costo portuario, en el ajuste tarifario "t". | ∑ef [(COA + CP ) ∗ TCR ] COAB = r=ep i,r i,r t i,t ∑ef QI r=ep i,r
11 | Costo de adquisición por litro del combustible "i" en el ajuste tarifario "t". | H COAi,t = ∑ γh ∗ COAh,t h=1
12 | Diferencial de precio del combustible "i" en el ajuste tarifario "t". | ∑c [(CIPi,d − COAi,d) ∗ SRi,d] DA = d=p i,t VSEi,t
13 | Costo promedio del inventario en colones del combustible "i" en tanque, para el día "d". | VIi,d CIPi,d = Inv i,d
14 | Valor del inventario del combustible "i" al costo sin impuesto, en colones, para el día "d". | 𝑉𝐼𝑖,𝑑 = 𝑉𝐼𝑖,(𝑑−1) + 𝐶𝐶𝑖,𝑟,𝑑 + 𝐴𝐽𝑖,𝑓 − [𝑆𝑅𝑖,𝑑 ∗ ((𝑉𝐼𝑖,(𝑑−1) + 𝐶𝐶𝑖,𝑟,𝑑 )/( 𝐼𝑛𝑣𝑖,(𝑑−1) + 𝐸𝐿𝑖,𝑑 )) ] (Así reformada la fórmula anterior mediante resolución N° RE-0025-JD-2023 del 21 de febrero de 2023)
15 | Ajuste al costo de los inventarios al final de cada mes de cálculo para el combustible "i". | AJi,f = (SInvi,f − VICi,f)
16 | Cantidad de litros de inventario del combustible "i" al final del día "d". Si para algún "i" Invi,d= 0, entonces CIPi,d = 0. | Invi,d = (Invi,(d−1) + ELi,d + AJLi,f − SRi,d)
[imagen]
[imagen]
[imagen]
[imagen]
23 | Ajuste por liquidación del canon de regulación, para el combustible "i" en el ajuste tarifario "t". | LCi,t = ∑um [(VTRi,b − VTEi,b ) ∗ b=pm (CAi,b) ]
24 | Promedio ponderado mensual del componente "x" del combustible "i", en el mes "n" a liquidar, según corresponda. | gu VRPi,g CXi,n = ∑ [CXi,g ∗ VTR ] g=gp i,n
25 | Subsidio específico por tipo de combustible "i" otorgado por el Estado mediante transferencia directa a Recope para el ajuste tarifario "t". | SE = VTSi,t i,t VTEi,t
26 | Subsidio cruzado por tipo de combustible "i", para el ajuste tarifario "t". | SCi,t = Si,t ∗ PPSi,t
27 | Valor total del subsidio para el ajuste tarifario "t". | I VTSt = ∑ SCi,t ∗ VTEi,t i=1
28 | Asignación del subsidio del combustible "i", para el ajuste tarifario "t". Únicamente participan los combustibles "i" no subsidiados. | VTSt ∗ PRVTi,t ASi,t = VTE i,t
29 | Margen de operación de Recope por litro de combustible "i", en el ajuste tarifario "t". | MOi,t = (ATDi,t+GAi,t + GPi,t) ∗ (1 − EFIt)+CDi,t + DEPi,t+CAJ i,t + PETi,t + OCi,t
30 | Pérdidas en tránsito para el combustible "i", en el ajuste tarifario "t". | 𝑃𝐸𝑇𝑖,𝑡 = 𝐶𝑂𝐴𝑃𝑖,𝑡 ∗ 𝑃𝑃𝐸𝑇𝑖,𝑡 (Así reformada la fórmula anterior mediante resolución N° RE-0025-JD-2023 del 21 de febrero de 2023)
[imagen]
[imagen]
[imagen]
[imagen]
[imagen]
[imagen]
[imagen]
[imagen]
[imagen]
31 | Eficiencia esperada en la disminución de costos, en el ajuste tarifario "t". | p−3 1 ∑z=p−1[(PTLz∗PTPz)2] EFIt = 3 − 1
32 | Índice Laspeyres de Productividad Total de los Factores para el periodo base "z". | ∑iu MOi,z−1∗VTRi,z PTL = [ i=ip ]/ z ∑xu PIN ∗QIN x=xp x,z−1 x,z ∑iu MOi,z−1∗VTRi,z−1 [ i=ip ] [imagen] ∑xuxp PINx,z−1∗QINx,z−1 x=
33 | Índice Paasche de Productividad Total de los Factores para el periodo base "z" | ∑iu MOi,z∗VTRi,z PTP = [ i=ip ]/ z ∑xu PIN ∗QIN x=xp x,z x,z ∑iu MOi,z∗VTRi,z−1 [ i=ip ] [imagen] ∑xuxp PINx,z∗QINx,z−1 x=
34 | Rendimiento sobre la base tarifaria del combustible "i" para el ajuste tarifario "t". | Rt ∗ (AFNORi,t + CTi,t) RSBTi,t = VAE i,t
35 | Tasa de rédito para el desarrollo para el ajuste tarifario "t". | VDt Rt = KDt ∗ (1 − TIt) ∗ VD + VCP + KEt t t VCPt ∗ VDt + VCPt
36 | Costo del endeudamiento para el ajuste tarifario "t". | ∑Q Dw,t ∗ Rw,t KDt = w=1 ∑Q Dw,t w
37 | Tasa colonizada para la deuda "w". | Rw = TB$w ∗ EDt + (TB$w + EDt)
38 | Costo del capital propio, en dólares para el ajuste tarifario "t". | KE$t = RFt + βAt ∗ (PMEt)
39 | Beta apalancada para el ajuste tarifario "t". | VD𝐭 βAt = βDt ∗ [1 + (1 − TIt) ∗ VCP ] 𝐭
[imagen]
[imagen]
[imagen]
[imagen]
[imagen]
Fórmula No. | Descripción | Detalle de la fórmula
40 | Costo de capital propio para el ajuste tarifario "t". | KEt = KE$t ∗ EDt + (KE$t + EDt)
41 | Activo fijo neto de operación al costo revaluado del combustible "i" para el ajuste tarifario "t". | AFNORi,t = AFNi,(p−1) + ADi,t − REi,t - DPAi,t
42 | Adiciones a reconocer del combustible "i" para el ajuste tarifario "t". | ADi,t = ADIi,t + ADPEi,t
43 | Adiciones ajustadas por el porcentaje de ejecución a reconocer del combustible "i" para el ajuste tarifario "t". | ADPEi,t = ADDi,t ∗ EJEi,t
44 | Porcentaje de ejecución promedio a reconocer del combustible "i", para el ajuste tarifario "t", de los últimos 5 periodos base. | ∑p−1 ADRi,z z=p−5 (ADEi,z ) EJEi,t = 5
45 | Capital de trabajo para el combustible "i", en el ajuste tarifario "t". | CTi,t = (VTPi,t ∗ PPAi,t ) ∗ DIPi,t
46 | Días de inventario promedio real en los 12 meses anteriores a la presentación del estudio tarifario, siempre que los datos no excedan de 4 meses de antigüedad. | DVi,t DIPi,t = VTRPi,t ( INCi,t )
47 | Ajuste por liquidación ordinaria del combustible "i", en el ajuste tarifario "t". | LRSBTi,a,t + LAEi,a,t ALOi,t = VAE i,t
