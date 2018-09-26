//Ojos
//Parte Negra
color([0,0,0]) translate([-11,0,2.2]) scale([0.5,1,1]) cylinder(1.1,2,2,center=true,$fn=100);
color([0,0,0]) translate([11,0,2.2]) scale([0.5,1,1]) cylinder(1.1,2,2,center=true,$fn=100); 
//Parte Blanca
color([1,1,1]) translate([-11,0,2.2]) scale([1.1,2,1]) cylinder(1,2,2,center=true,$fn=100); 
color([1,1,1]) translate([11,0,2.2]) scale([1.1,2,1]) cylinder(1,2,2,center=true,$fn=100);

//Tallo
color([21/250,81/250,126/250])

translate([0,-4,-2.3]) cube([2.5,25,0.3],center=true);

//Hojas
 translate([0,10,-2.3]) rotate([0,0,0]) hoja();
 translate([9,2,-2.3]) rotate([0,0,-60]) hoja();
 translate([-9,2,-2.3]) rotate([0,0,60]) hoja();
 translate([9,-7.5,-2.3]) rotate([0,0,-60]) hoja();
 translate([-9,-7.5,-2.3]) rotate([0,0,60]) hoja();

//Esfera central
color([21/250,81/250,126/250]) translate([0,0,2.4]) sphere(4.6,$fn=100);
//Circulos interiores
for (i=[0:1:3])
    color([21/250,81/250,126/250])
    translate([11*cos(45+i*90),11*sin(45+i*90),2.2]) cylinder(1,2,2,center=true,$fn=100); 
//Esferas diametro grande
for (i=[0:1:5])
    color([19/250,54/250,99/250])
    translate([25*cos(30+i*60),25*sin(30+i*60),0]) sphere(5,$fn=100);
//Circuferencia
translate([0,0,1.9]) anillo(10.8,11);
//Cilindro pequeño
color([19/250,54/250,99/250]) cylinder(4.6,18,18,center=true,$fn=100);
//Cilindro grande
color([21/250,81/250,126/250]) cylinder(4,25,25,center=true,$fn=100);

module anillo(r1,r2){
union(){
    color([19/250,54/250,99/250]) cylinder(1+0.2,r1,r1,center=true,$fn=50);
    color([0,0,0]) cylinder(1       ,r2,r2,center=true,$fn=50);
}
}
module hoja(){
color([21/250,81/250,126/250]){
translate([0,-6,0]) cube([2,9,0.3],center=true);
scale([1/8,1/8,1/8])
linear_extrude(height = 2, center = true){
hull(){
circle(20, center = true,$fn=15);
polygon([[20,0],[16,12.5],[7,25],[0,40],[-7,25],[-16,12.5],[-20,0]]);
}
}
}
}