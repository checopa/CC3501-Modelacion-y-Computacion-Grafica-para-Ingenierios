rotate([240,30,0]) translate([0,0,12])rotate([0,0,-20])  cabeza();
rotate([120,30,0]) translate([0,0,12]) rotate([0,0,20]) cabeza();
translate([0,0,12]) cabeza();

//cabeza
module cabeza(){
rotate([-25,135,0]) translate([0,0,10]) scale([0.2,0.2,0.2]) tornillo();
rotate([25,135,0]) translate([0,0,10]) scale([0.2,0.2,0.2]) tornillo();
translate([0,0,10]) scale([0.3,0.3,0.2])tornillo();
rotate([-60,0,0])  translate([0,0,10]) rotate([0,0,-25]) scale([1,1.8,1.5]) iman();
rotate([60,0,0]) translate([0,0,10]) rotate([0,0,25]) scale([1,1.8,1.5]) iman();
ojo();
}

//Ojos
module ojo(){
    rotate([0,90,0])
    union(){
    color("black") translate([0,0,8.3]) semi(1);
    union(){
    color("white") semi(4.999);
    difference(){
    color ([63/250,71/250,70/250])  sphere(r=10,center=true,$fn=100);
    translate([0,0,18]) cube(20,center=true);   
        }
    }
}

}

//tornillo
    module tornillo(){
translate([0,0,5])
union(){
color ([56/250,50/250,41/250]) cylinder(11,r=3.5,center=true,$fn=50);
color ([56/250,50/250,41/250]) semi(5);
}
}
//semiesfera
module semi(R){
    difference(){
sphere(r=2*R,center=true,$fn=100);
translate([0,0,-R]) cube(4*R,center=true);
}
}
//Iman
module iman(){
rotate([90,0,90]) translate([0,4,0])
union(){
color("Blue") 
linear_extrude(2){
translate([-2,3.5]) square([2,2],center=true);}
color("Red") 
linear_extrude(2){
translate([2,3.5]) square([2,2],center=true);}
translate([2,0,0]) im();
translate([-2,0,0]) mirror([1,0,0]) im();
 }
 }

module im(){
color([49/250,47/250,45/250])
linear_extrude(2){
union(){
hull(){
translate([0,-3]) circle(1,center=true,$fn=100);
square([2,5],center=true);
}
hull(){
translate([0,-3]) circle(1,center=true,$fn=100);
translate([-2,-3]) square([1,2],center=true);
}
}
}
}

