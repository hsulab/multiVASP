#include "colors.inc"
#include "finish.inc"

global_settings {assumed_gamma 1 max_trace_level 6}
background {color White}
camera {perspective
  right -7.20*x up 7.12*y
  direction 50.00*z
  location <0,0,50.00> look_at <0,0,0>}
light_source {<  2.00,   3.00,  40.00> color White
  area_light <0.70, 0, 0>, <0, 0.70, 0>, 3, 3
  adaptive 1 jitter}

#declare simple = finish {phong 0.7}
#declare pale = finish {ambient .5 diffuse .85 roughness .001 specular 0.200 }
#declare intermediate = finish {ambient 0.3 diffuse 0.6 specular 0.10 roughness 0.04 }
#declare vmd = finish {ambient .0 diffuse .65 phong 0.1 phong_size 40. specular 0.500 }
#declare jmol = finish {ambient .2 diffuse .6 specular 1 roughness .001 metallic}
#declare ase2 = finish {ambient 0.05 brilliance 3 diffuse 0.6 metallic specular 0.70 roughness 0.04 reflection 0.15}
#declare ase3 = finish {ambient .15 brilliance 2 diffuse .6 metallic specular 1. roughness .001 reflection .0}
#declare glass = finish {ambient .05 diffuse .3 specular 1. roughness .001}
#declare glass2 = finish {ambient .0 diffuse .3 specular 1. reflection .25 roughness .001}
#declare Rcell = 0.100;
#declare Rbond = 0.200;

#macro atom(LOC, R, COL, TRANS, FIN)
  sphere{LOC, R texture{pigment{color COL transmit TRANS} finish{FIN}}}
#end
#macro constrain(LOC, R, COL, TRANS FIN)
union{torus{R, Rcell rotate 45*z texture{pigment{color COL transmit TRANS} finish{FIN}}}
      torus{R, Rcell rotate -45*z texture{pigment{color COL transmit TRANS} finish{FIN}}}
      translate LOC}
#end

atom(<  0.93,   2.19, -12.00>, 0.56, rgb <1.00, 0.05, 0.05>, 0.0, ase3) // #0 
atom(<  0.93,  -0.73, -12.00>, 0.56, rgb <1.00, 0.05, 0.05>, 0.0, ase3) // #1 
atom(< -1.00,   0.73, -10.78>, 0.56, rgb <1.00, 0.05, 0.05>, 0.0, ase3) // #2 
atom(< -1.00,  -2.19, -10.78>, 0.56, rgb <1.00, 0.05, 0.05>, 0.0, ase3) // #3 
atom(<  2.87,   0.73, -10.78>, 0.56, rgb <1.00, 0.05, 0.05>, 0.0, ase3) // #4 
atom(<  2.87,  -2.19, -10.78>, 0.56, rgb <1.00, 0.05, 0.05>, 0.0, ase3) // #5 
atom(<  0.93,   2.19,  -9.55>, 0.56, rgb <1.00, 0.05, 0.05>, 0.0, ase3) // #6 
atom(<  0.93,  -0.73,  -9.55>, 0.56, rgb <1.00, 0.05, 0.05>, 0.0, ase3) // #7 
atom(< -2.23,   2.19,  -8.85>, 0.56, rgb <1.00, 0.05, 0.05>, 0.0, ase3) // #8 
atom(< -2.23,  -0.73,  -8.85>, 0.56, rgb <1.00, 0.05, 0.05>, 0.0, ase3) // #9 
atom(< -0.29,   0.73,  -7.62>, 0.56, rgb <1.00, 0.05, 0.05>, 0.0, ase3) // #10 
atom(< -0.29,  -2.19,  -7.62>, 0.56, rgb <1.00, 0.05, 0.05>, 0.0, ase3) // #11 
atom(<  2.16,   0.73,  -7.62>, 0.56, rgb <1.00, 0.05, 0.05>, 0.0, ase3) // #12 
atom(<  2.16,  -2.19,  -7.62>, 0.56, rgb <1.00, 0.05, 0.05>, 0.0, ase3) // #13 
atom(< -2.23,   2.19,  -6.39>, 0.56, rgb <1.00, 0.05, 0.05>, 0.0, ase3) // #14 
atom(< -2.23,  -0.73,  -6.39>, 0.56, rgb <1.00, 0.05, 0.05>, 0.0, ase3) // #15 
atom(<  0.93,   2.19,  -5.70>, 0.56, rgb <1.00, 0.05, 0.05>, 0.0, ase3) // #16 
atom(<  0.93,  -0.73,  -5.70>, 0.56, rgb <1.00, 0.05, 0.05>, 0.0, ase3) // #17 
atom(< -0.99,   0.73,  -4.46>, 0.56, rgb <1.00, 0.05, 0.05>, 0.0, ase3) // #18 
atom(< -0.99,  -2.19,  -4.46>, 0.56, rgb <1.00, 0.05, 0.05>, 0.0, ase3) // #19 
atom(<  2.85,   0.73,  -4.46>, 0.56, rgb <1.00, 0.05, 0.05>, 0.0, ase3) // #20 
atom(<  2.85,  -2.19,  -4.46>, 0.56, rgb <1.00, 0.05, 0.05>, 0.0, ase3) // #21 
atom(<  0.93,   2.19,  -3.27>, 0.56, rgb <1.00, 0.05, 0.05>, 0.0, ase3) // #22 
atom(<  0.93,  -0.73,  -3.27>, 0.56, rgb <1.00, 0.05, 0.05>, 0.0, ase3) // #23 
atom(< -2.23,   2.19,  -2.49>, 0.56, rgb <1.00, 0.05, 0.05>, 0.0, ase3) // #24 
atom(< -2.23,  -0.73,  -2.49>, 0.56, rgb <1.00, 0.05, 0.05>, 0.0, ase3) // #25 
atom(< -0.24,   0.73,  -1.14>, 0.56, rgb <1.00, 0.05, 0.05>, 0.0, ase3) // #26 
atom(< -0.24,  -2.19,  -1.14>, 0.56, rgb <1.00, 0.05, 0.05>, 0.0, ase3) // #27 
atom(<  2.11,   0.73,  -1.14>, 0.56, rgb <1.00, 0.05, 0.05>, 0.0, ase3) // #28 
atom(<  2.11,  -2.19,  -1.14>, 0.56, rgb <1.00, 0.05, 0.05>, 0.0, ase3) // #29 
atom(< -2.23,   2.19,   0.00>, 0.56, rgb <1.00, 0.05, 0.05>, 0.0, ase3) // #30 
atom(< -2.23,  -0.73,  -0.00>, 0.56, rgb <1.00, 0.05, 0.05>, 0.0, ase3) // #31 
atom(< -2.23,   2.19, -10.78>, 1.20, rgb <0.09, 0.33, 0.53>, 0.0, ase3) // #32 
atom(< -2.23,  -0.73, -10.78>, 1.20, rgb <0.09, 0.33, 0.53>, 0.0, ase3) // #33 
atom(<  0.93,   0.73, -10.78>, 1.20, rgb <0.09, 0.33, 0.53>, 0.0, ase3) // #34 
atom(<  0.93,  -2.19, -10.78>, 1.20, rgb <0.09, 0.33, 0.53>, 0.0, ase3) // #35 
atom(< -2.23,   0.73,  -7.62>, 1.20, rgb <0.09, 0.33, 0.53>, 0.0, ase3) // #36 
atom(< -2.23,  -2.19,  -7.62>, 1.20, rgb <0.09, 0.33, 0.53>, 0.0, ase3) // #37 
atom(<  0.93,   2.19,  -7.62>, 1.20, rgb <0.09, 0.33, 0.53>, 0.0, ase3) // #38 
atom(<  0.93,  -0.73,  -7.62>, 1.20, rgb <0.09, 0.33, 0.53>, 0.0, ase3) // #39 
atom(< -2.23,   2.19,  -4.40>, 1.20, rgb <0.09, 0.33, 0.53>, 0.0, ase3) // #40 
atom(< -2.23,  -0.73,  -4.40>, 1.20, rgb <0.09, 0.33, 0.53>, 0.0, ase3) // #41 
atom(<  0.93,   0.73,  -4.52>, 1.20, rgb <0.09, 0.33, 0.53>, 0.0, ase3) // #42 
atom(<  0.93,  -2.19,  -4.52>, 1.20, rgb <0.09, 0.33, 0.53>, 0.0, ase3) // #43 
atom(< -2.23,   0.73,  -1.11>, 1.20, rgb <0.09, 0.33, 0.53>, 0.0, ase3) // #44 
atom(< -2.23,  -2.19,  -1.11>, 1.20, rgb <0.09, 0.33, 0.53>, 0.0, ase3) // #45 
atom(<  0.93,   2.19,  -1.43>, 1.20, rgb <0.09, 0.33, 0.53>, 0.0, ase3) // #46 
atom(<  0.93,  -0.73,  -1.43>, 1.02, rgb <0.40, 0.56, 0.56>, 0.0, ase3) // #47 
cylinder {< -2.23,   2.19, -10.78>, < -1.62,   1.46, -10.78>, Rbond texture{pigment {color rgb <0.09, 0.33, 0.53> transmit 0.0} finish{ase3}}}
cylinder {< -1.00,   0.73, -10.78>, < -1.62,   1.46, -10.78>, Rbond texture{pigment {color rgb <1.00, 0.05, 0.05> transmit 0.0} finish{ase3}}}
cylinder {< -2.23,   2.19, -10.78>, < -2.23,   2.19,  -9.81>, Rbond texture{pigment {color rgb <0.09, 0.33, 0.53> transmit 0.0} finish{ase3}}}
cylinder {< -2.23,   2.19,  -8.85>, < -2.23,   2.19,  -9.81>, Rbond texture{pigment {color rgb <1.00, 0.05, 0.05> transmit 0.0} finish{ase3}}}
cylinder {< -2.23,  -0.73, -10.78>, < -1.62,  -0.00, -10.78>, Rbond texture{pigment {color rgb <0.09, 0.33, 0.53> transmit 0.0} finish{ase3}}}
cylinder {< -1.00,   0.73, -10.78>, < -1.62,  -0.00, -10.78>, Rbond texture{pigment {color rgb <1.00, 0.05, 0.05> transmit 0.0} finish{ase3}}}
cylinder {< -2.23,  -0.73, -10.78>, < -1.62,  -1.46, -10.78>, Rbond texture{pigment {color rgb <0.09, 0.33, 0.53> transmit 0.0} finish{ase3}}}
cylinder {< -1.00,  -2.19, -10.78>, < -1.62,  -1.46, -10.78>, Rbond texture{pigment {color rgb <1.00, 0.05, 0.05> transmit 0.0} finish{ase3}}}
cylinder {< -2.23,  -0.73, -10.78>, < -2.23,  -0.73,  -9.81>, Rbond texture{pigment {color rgb <0.09, 0.33, 0.53> transmit 0.0} finish{ase3}}}
cylinder {< -2.23,  -0.73,  -8.85>, < -2.23,  -0.73,  -9.81>, Rbond texture{pigment {color rgb <1.00, 0.05, 0.05> transmit 0.0} finish{ase3}}}
cylinder {<  0.93,   0.73, -10.78>, <  0.93,   1.46, -11.39>, Rbond texture{pigment {color rgb <0.09, 0.33, 0.53> transmit 0.0} finish{ase3}}}
cylinder {<  0.93,   2.19, -12.00>, <  0.93,   1.46, -11.39>, Rbond texture{pigment {color rgb <1.00, 0.05, 0.05> transmit 0.0} finish{ase3}}}
cylinder {<  0.93,   0.73, -10.78>, <  0.93,  -0.00, -11.39>, Rbond texture{pigment {color rgb <0.09, 0.33, 0.53> transmit 0.0} finish{ase3}}}
cylinder {<  0.93,  -0.73, -12.00>, <  0.93,  -0.00, -11.39>, Rbond texture{pigment {color rgb <1.00, 0.05, 0.05> transmit 0.0} finish{ase3}}}
cylinder {<  0.93,   0.73, -10.78>, < -0.04,   0.73, -10.78>, Rbond texture{pigment {color rgb <0.09, 0.33, 0.53> transmit 0.0} finish{ase3}}}
cylinder {< -1.00,   0.73, -10.78>, < -0.04,   0.73, -10.78>, Rbond texture{pigment {color rgb <1.00, 0.05, 0.05> transmit 0.0} finish{ase3}}}
cylinder {<  0.93,   0.73, -10.78>, <  1.90,   0.73, -10.78>, Rbond texture{pigment {color rgb <0.09, 0.33, 0.53> transmit 0.0} finish{ase3}}}
cylinder {<  2.87,   0.73, -10.78>, <  1.90,   0.73, -10.78>, Rbond texture{pigment {color rgb <1.00, 0.05, 0.05> transmit 0.0} finish{ase3}}}
cylinder {<  0.93,   0.73, -10.78>, <  0.93,   1.46, -10.17>, Rbond texture{pigment {color rgb <0.09, 0.33, 0.53> transmit 0.0} finish{ase3}}}
cylinder {<  0.93,   2.19,  -9.55>, <  0.93,   1.46, -10.17>, Rbond texture{pigment {color rgb <1.00, 0.05, 0.05> transmit 0.0} finish{ase3}}}
cylinder {<  0.93,   0.73, -10.78>, <  0.93,  -0.00, -10.17>, Rbond texture{pigment {color rgb <0.09, 0.33, 0.53> transmit 0.0} finish{ase3}}}
cylinder {<  0.93,  -0.73,  -9.55>, <  0.93,  -0.00, -10.17>, Rbond texture{pigment {color rgb <1.00, 0.05, 0.05> transmit 0.0} finish{ase3}}}
cylinder {<  0.93,  -2.19, -10.78>, <  0.93,  -1.46, -11.39>, Rbond texture{pigment {color rgb <0.09, 0.33, 0.53> transmit 0.0} finish{ase3}}}
cylinder {<  0.93,  -0.73, -12.00>, <  0.93,  -1.46, -11.39>, Rbond texture{pigment {color rgb <1.00, 0.05, 0.05> transmit 0.0} finish{ase3}}}
cylinder {<  0.93,  -2.19, -10.78>, < -0.04,  -2.19, -10.78>, Rbond texture{pigment {color rgb <0.09, 0.33, 0.53> transmit 0.0} finish{ase3}}}
cylinder {< -1.00,  -2.19, -10.78>, < -0.04,  -2.19, -10.78>, Rbond texture{pigment {color rgb <1.00, 0.05, 0.05> transmit 0.0} finish{ase3}}}
cylinder {<  0.93,  -2.19, -10.78>, <  1.90,  -2.19, -10.78>, Rbond texture{pigment {color rgb <0.09, 0.33, 0.53> transmit 0.0} finish{ase3}}}
cylinder {<  2.87,  -2.19, -10.78>, <  1.90,  -2.19, -10.78>, Rbond texture{pigment {color rgb <1.00, 0.05, 0.05> transmit 0.0} finish{ase3}}}
cylinder {<  0.93,  -2.19, -10.78>, <  0.93,  -1.46, -10.17>, Rbond texture{pigment {color rgb <0.09, 0.33, 0.53> transmit 0.0} finish{ase3}}}
cylinder {<  0.93,  -0.73,  -9.55>, <  0.93,  -1.46, -10.17>, Rbond texture{pigment {color rgb <1.00, 0.05, 0.05> transmit 0.0} finish{ase3}}}
cylinder {< -2.23,   0.73,  -7.62>, < -2.23,   1.46,  -8.23>, Rbond texture{pigment {color rgb <0.09, 0.33, 0.53> transmit 0.0} finish{ase3}}}
cylinder {< -2.23,   2.19,  -8.85>, < -2.23,   1.46,  -8.23>, Rbond texture{pigment {color rgb <1.00, 0.05, 0.05> transmit 0.0} finish{ase3}}}
cylinder {< -2.23,   0.73,  -7.62>, < -2.23,  -0.00,  -8.23>, Rbond texture{pigment {color rgb <0.09, 0.33, 0.53> transmit 0.0} finish{ase3}}}
cylinder {< -2.23,  -0.73,  -8.85>, < -2.23,  -0.00,  -8.23>, Rbond texture{pigment {color rgb <1.00, 0.05, 0.05> transmit 0.0} finish{ase3}}}
cylinder {< -2.23,   0.73,  -7.62>, < -1.26,   0.73,  -7.62>, Rbond texture{pigment {color rgb <0.09, 0.33, 0.53> transmit 0.0} finish{ase3}}}
cylinder {< -0.29,   0.73,  -7.62>, < -1.26,   0.73,  -7.62>, Rbond texture{pigment {color rgb <1.00, 0.05, 0.05> transmit 0.0} finish{ase3}}}
cylinder {< -2.23,   0.73,  -7.62>, < -2.23,   1.46,  -7.01>, Rbond texture{pigment {color rgb <0.09, 0.33, 0.53> transmit 0.0} finish{ase3}}}
cylinder {< -2.23,   2.19,  -6.39>, < -2.23,   1.46,  -7.01>, Rbond texture{pigment {color rgb <1.00, 0.05, 0.05> transmit 0.0} finish{ase3}}}
cylinder {< -2.23,   0.73,  -7.62>, < -2.23,  -0.00,  -7.01>, Rbond texture{pigment {color rgb <0.09, 0.33, 0.53> transmit 0.0} finish{ase3}}}
cylinder {< -2.23,  -0.73,  -6.39>, < -2.23,  -0.00,  -7.01>, Rbond texture{pigment {color rgb <1.00, 0.05, 0.05> transmit 0.0} finish{ase3}}}
cylinder {< -2.23,  -2.19,  -7.62>, < -2.23,  -1.46,  -8.23>, Rbond texture{pigment {color rgb <0.09, 0.33, 0.53> transmit 0.0} finish{ase3}}}
cylinder {< -2.23,  -0.73,  -8.85>, < -2.23,  -1.46,  -8.23>, Rbond texture{pigment {color rgb <1.00, 0.05, 0.05> transmit 0.0} finish{ase3}}}
cylinder {< -2.23,  -2.19,  -7.62>, < -1.26,  -2.19,  -7.62>, Rbond texture{pigment {color rgb <0.09, 0.33, 0.53> transmit 0.0} finish{ase3}}}
cylinder {< -0.29,  -2.19,  -7.62>, < -1.26,  -2.19,  -7.62>, Rbond texture{pigment {color rgb <1.00, 0.05, 0.05> transmit 0.0} finish{ase3}}}
cylinder {< -2.23,  -2.19,  -7.62>, < -2.23,  -1.46,  -7.01>, Rbond texture{pigment {color rgb <0.09, 0.33, 0.53> transmit 0.0} finish{ase3}}}
cylinder {< -2.23,  -0.73,  -6.39>, < -2.23,  -1.46,  -7.01>, Rbond texture{pigment {color rgb <1.00, 0.05, 0.05> transmit 0.0} finish{ase3}}}
cylinder {<  0.93,   2.19,  -7.62>, <  0.93,   2.19,  -8.59>, Rbond texture{pigment {color rgb <0.09, 0.33, 0.53> transmit 0.0} finish{ase3}}}
cylinder {<  0.93,   2.19,  -9.55>, <  0.93,   2.19,  -8.59>, Rbond texture{pigment {color rgb <1.00, 0.05, 0.05> transmit 0.0} finish{ase3}}}
cylinder {<  0.93,   2.19,  -7.62>, <  0.32,   1.46,  -7.62>, Rbond texture{pigment {color rgb <0.09, 0.33, 0.53> transmit 0.0} finish{ase3}}}
cylinder {< -0.29,   0.73,  -7.62>, <  0.32,   1.46,  -7.62>, Rbond texture{pigment {color rgb <1.00, 0.05, 0.05> transmit 0.0} finish{ase3}}}
cylinder {<  0.93,   2.19,  -7.62>, <  1.54,   1.46,  -7.62>, Rbond texture{pigment {color rgb <0.09, 0.33, 0.53> transmit 0.0} finish{ase3}}}
cylinder {<  2.16,   0.73,  -7.62>, <  1.54,   1.46,  -7.62>, Rbond texture{pigment {color rgb <1.00, 0.05, 0.05> transmit 0.0} finish{ase3}}}
cylinder {<  0.93,   2.19,  -7.62>, <  0.93,   2.19,  -6.66>, Rbond texture{pigment {color rgb <0.09, 0.33, 0.53> transmit 0.0} finish{ase3}}}
cylinder {<  0.93,   2.19,  -5.70>, <  0.93,   2.19,  -6.66>, Rbond texture{pigment {color rgb <1.00, 0.05, 0.05> transmit 0.0} finish{ase3}}}
cylinder {<  0.93,  -0.73,  -7.62>, <  0.93,  -0.73,  -8.59>, Rbond texture{pigment {color rgb <0.09, 0.33, 0.53> transmit 0.0} finish{ase3}}}
cylinder {<  0.93,  -0.73,  -9.55>, <  0.93,  -0.73,  -8.59>, Rbond texture{pigment {color rgb <1.00, 0.05, 0.05> transmit 0.0} finish{ase3}}}
cylinder {<  0.93,  -0.73,  -7.62>, <  0.32,  -0.00,  -7.62>, Rbond texture{pigment {color rgb <0.09, 0.33, 0.53> transmit 0.0} finish{ase3}}}
cylinder {< -0.29,   0.73,  -7.62>, <  0.32,  -0.00,  -7.62>, Rbond texture{pigment {color rgb <1.00, 0.05, 0.05> transmit 0.0} finish{ase3}}}
cylinder {<  0.93,  -0.73,  -7.62>, <  0.32,  -1.46,  -7.62>, Rbond texture{pigment {color rgb <0.09, 0.33, 0.53> transmit 0.0} finish{ase3}}}
cylinder {< -0.29,  -2.19,  -7.62>, <  0.32,  -1.46,  -7.62>, Rbond texture{pigment {color rgb <1.00, 0.05, 0.05> transmit 0.0} finish{ase3}}}
cylinder {<  0.93,  -0.73,  -7.62>, <  1.54,  -0.00,  -7.62>, Rbond texture{pigment {color rgb <0.09, 0.33, 0.53> transmit 0.0} finish{ase3}}}
cylinder {<  2.16,   0.73,  -7.62>, <  1.54,  -0.00,  -7.62>, Rbond texture{pigment {color rgb <1.00, 0.05, 0.05> transmit 0.0} finish{ase3}}}
cylinder {<  0.93,  -0.73,  -7.62>, <  1.54,  -1.46,  -7.62>, Rbond texture{pigment {color rgb <0.09, 0.33, 0.53> transmit 0.0} finish{ase3}}}
cylinder {<  2.16,  -2.19,  -7.62>, <  1.54,  -1.46,  -7.62>, Rbond texture{pigment {color rgb <1.00, 0.05, 0.05> transmit 0.0} finish{ase3}}}
cylinder {<  0.93,  -0.73,  -7.62>, <  0.93,  -0.73,  -6.66>, Rbond texture{pigment {color rgb <0.09, 0.33, 0.53> transmit 0.0} finish{ase3}}}
cylinder {<  0.93,  -0.73,  -5.70>, <  0.93,  -0.73,  -6.66>, Rbond texture{pigment {color rgb <1.00, 0.05, 0.05> transmit 0.0} finish{ase3}}}
cylinder {< -2.23,   2.19,  -4.40>, < -2.23,   2.19,  -5.40>, Rbond texture{pigment {color rgb <0.09, 0.33, 0.53> transmit 0.0} finish{ase3}}}
cylinder {< -2.23,   2.19,  -6.39>, < -2.23,   2.19,  -5.40>, Rbond texture{pigment {color rgb <1.00, 0.05, 0.05> transmit 0.0} finish{ase3}}}
cylinder {< -2.23,   2.19,  -4.40>, < -1.61,   1.46,  -4.43>, Rbond texture{pigment {color rgb <0.09, 0.33, 0.53> transmit 0.0} finish{ase3}}}
cylinder {< -0.99,   0.73,  -4.46>, < -1.61,   1.46,  -4.43>, Rbond texture{pigment {color rgb <1.00, 0.05, 0.05> transmit 0.0} finish{ase3}}}
cylinder {< -2.23,   2.19,  -4.40>, < -2.23,   2.19,  -3.44>, Rbond texture{pigment {color rgb <0.09, 0.33, 0.53> transmit 0.0} finish{ase3}}}
cylinder {< -2.23,   2.19,  -2.49>, < -2.23,   2.19,  -3.44>, Rbond texture{pigment {color rgb <1.00, 0.05, 0.05> transmit 0.0} finish{ase3}}}
cylinder {< -2.23,  -0.73,  -4.40>, < -2.23,  -0.73,  -5.40>, Rbond texture{pigment {color rgb <0.09, 0.33, 0.53> transmit 0.0} finish{ase3}}}
cylinder {< -2.23,  -0.73,  -6.39>, < -2.23,  -0.73,  -5.40>, Rbond texture{pigment {color rgb <1.00, 0.05, 0.05> transmit 0.0} finish{ase3}}}
cylinder {< -2.23,  -0.73,  -4.40>, < -1.61,   0.00,  -4.43>, Rbond texture{pigment {color rgb <0.09, 0.33, 0.53> transmit 0.0} finish{ase3}}}
cylinder {< -0.99,   0.73,  -4.46>, < -1.61,   0.00,  -4.43>, Rbond texture{pigment {color rgb <1.00, 0.05, 0.05> transmit 0.0} finish{ase3}}}
cylinder {< -2.23,  -0.73,  -4.40>, < -1.61,  -1.46,  -4.43>, Rbond texture{pigment {color rgb <0.09, 0.33, 0.53> transmit 0.0} finish{ase3}}}
cylinder {< -0.99,  -2.19,  -4.46>, < -1.61,  -1.46,  -4.43>, Rbond texture{pigment {color rgb <1.00, 0.05, 0.05> transmit 0.0} finish{ase3}}}
cylinder {< -2.23,  -0.73,  -4.40>, < -2.23,  -0.73,  -3.44>, Rbond texture{pigment {color rgb <0.09, 0.33, 0.53> transmit 0.0} finish{ase3}}}
cylinder {< -2.23,  -0.73,  -2.49>, < -2.23,  -0.73,  -3.44>, Rbond texture{pigment {color rgb <1.00, 0.05, 0.05> transmit 0.0} finish{ase3}}}
cylinder {<  0.93,   0.73,  -4.52>, <  0.93,   1.46,  -5.11>, Rbond texture{pigment {color rgb <0.09, 0.33, 0.53> transmit 0.0} finish{ase3}}}
cylinder {<  0.93,   2.19,  -5.70>, <  0.93,   1.46,  -5.11>, Rbond texture{pigment {color rgb <1.00, 0.05, 0.05> transmit 0.0} finish{ase3}}}
cylinder {<  0.93,   0.73,  -4.52>, <  0.93,  -0.00,  -5.11>, Rbond texture{pigment {color rgb <0.09, 0.33, 0.53> transmit 0.0} finish{ase3}}}
cylinder {<  0.93,  -0.73,  -5.70>, <  0.93,  -0.00,  -5.11>, Rbond texture{pigment {color rgb <1.00, 0.05, 0.05> transmit 0.0} finish{ase3}}}
cylinder {<  0.93,   0.73,  -4.52>, < -0.03,   0.73,  -4.49>, Rbond texture{pigment {color rgb <0.09, 0.33, 0.53> transmit 0.0} finish{ase3}}}
cylinder {< -0.99,   0.73,  -4.46>, < -0.03,   0.73,  -4.49>, Rbond texture{pigment {color rgb <1.00, 0.05, 0.05> transmit 0.0} finish{ase3}}}
cylinder {<  0.93,   0.73,  -4.52>, <  1.89,   0.73,  -4.49>, Rbond texture{pigment {color rgb <0.09, 0.33, 0.53> transmit 0.0} finish{ase3}}}
cylinder {<  2.85,   0.73,  -4.46>, <  1.89,   0.73,  -4.49>, Rbond texture{pigment {color rgb <1.00, 0.05, 0.05> transmit 0.0} finish{ase3}}}
cylinder {<  0.93,   0.73,  -4.52>, <  0.93,   1.46,  -3.89>, Rbond texture{pigment {color rgb <0.09, 0.33, 0.53> transmit 0.0} finish{ase3}}}
cylinder {<  0.93,   2.19,  -3.27>, <  0.93,   1.46,  -3.89>, Rbond texture{pigment {color rgb <1.00, 0.05, 0.05> transmit 0.0} finish{ase3}}}
cylinder {<  0.93,   0.73,  -4.52>, <  0.93,   0.00,  -3.89>, Rbond texture{pigment {color rgb <0.09, 0.33, 0.53> transmit 0.0} finish{ase3}}}
cylinder {<  0.93,  -0.73,  -3.27>, <  0.93,   0.00,  -3.89>, Rbond texture{pigment {color rgb <1.00, 0.05, 0.05> transmit 0.0} finish{ase3}}}
cylinder {<  0.93,  -2.19,  -4.52>, <  0.93,  -1.46,  -5.11>, Rbond texture{pigment {color rgb <0.09, 0.33, 0.53> transmit 0.0} finish{ase3}}}
cylinder {<  0.93,  -0.73,  -5.70>, <  0.93,  -1.46,  -5.11>, Rbond texture{pigment {color rgb <1.00, 0.05, 0.05> transmit 0.0} finish{ase3}}}
cylinder {<  0.93,  -2.19,  -4.52>, < -0.03,  -2.19,  -4.49>, Rbond texture{pigment {color rgb <0.09, 0.33, 0.53> transmit 0.0} finish{ase3}}}
cylinder {< -0.99,  -2.19,  -4.46>, < -0.03,  -2.19,  -4.49>, Rbond texture{pigment {color rgb <1.00, 0.05, 0.05> transmit 0.0} finish{ase3}}}
cylinder {<  0.93,  -2.19,  -4.52>, <  1.89,  -2.19,  -4.49>, Rbond texture{pigment {color rgb <0.09, 0.33, 0.53> transmit 0.0} finish{ase3}}}
cylinder {<  2.85,  -2.19,  -4.46>, <  1.89,  -2.19,  -4.49>, Rbond texture{pigment {color rgb <1.00, 0.05, 0.05> transmit 0.0} finish{ase3}}}
cylinder {<  0.93,  -2.19,  -4.52>, <  0.93,  -1.46,  -3.89>, Rbond texture{pigment {color rgb <0.09, 0.33, 0.53> transmit 0.0} finish{ase3}}}
cylinder {<  0.93,  -0.73,  -3.27>, <  0.93,  -1.46,  -3.89>, Rbond texture{pigment {color rgb <1.00, 0.05, 0.05> transmit 0.0} finish{ase3}}}
cylinder {< -2.23,   0.73,  -1.11>, < -2.23,   1.46,  -1.80>, Rbond texture{pigment {color rgb <0.09, 0.33, 0.53> transmit 0.0} finish{ase3}}}
cylinder {< -2.23,   2.19,  -2.49>, < -2.23,   1.46,  -1.80>, Rbond texture{pigment {color rgb <1.00, 0.05, 0.05> transmit 0.0} finish{ase3}}}
cylinder {< -2.23,   0.73,  -1.11>, < -2.23,   0.00,  -1.80>, Rbond texture{pigment {color rgb <0.09, 0.33, 0.53> transmit 0.0} finish{ase3}}}
cylinder {< -2.23,  -0.73,  -2.49>, < -2.23,   0.00,  -1.80>, Rbond texture{pigment {color rgb <1.00, 0.05, 0.05> transmit 0.0} finish{ase3}}}
cylinder {< -2.23,   0.73,  -1.11>, < -1.23,   0.73,  -1.12>, Rbond texture{pigment {color rgb <0.09, 0.33, 0.53> transmit 0.0} finish{ase3}}}
cylinder {< -0.24,   0.73,  -1.14>, < -1.23,   0.73,  -1.12>, Rbond texture{pigment {color rgb <1.00, 0.05, 0.05> transmit 0.0} finish{ase3}}}
cylinder {< -2.23,   0.73,  -1.11>, < -2.23,   1.46,  -0.55>, Rbond texture{pigment {color rgb <0.09, 0.33, 0.53> transmit 0.0} finish{ase3}}}
cylinder {< -2.23,   2.19,   0.00>, < -2.23,   1.46,  -0.55>, Rbond texture{pigment {color rgb <1.00, 0.05, 0.05> transmit 0.0} finish{ase3}}}
cylinder {< -2.23,   0.73,  -1.11>, < -2.23,   0.00,  -0.55>, Rbond texture{pigment {color rgb <0.09, 0.33, 0.53> transmit 0.0} finish{ase3}}}
cylinder {< -2.23,  -0.73,  -0.00>, < -2.23,   0.00,  -0.55>, Rbond texture{pigment {color rgb <1.00, 0.05, 0.05> transmit 0.0} finish{ase3}}}
cylinder {< -2.23,  -2.19,  -1.11>, < -2.23,  -1.46,  -1.80>, Rbond texture{pigment {color rgb <0.09, 0.33, 0.53> transmit 0.0} finish{ase3}}}
cylinder {< -2.23,  -0.73,  -2.49>, < -2.23,  -1.46,  -1.80>, Rbond texture{pigment {color rgb <1.00, 0.05, 0.05> transmit 0.0} finish{ase3}}}
cylinder {< -2.23,  -2.19,  -1.11>, < -1.23,  -2.19,  -1.12>, Rbond texture{pigment {color rgb <0.09, 0.33, 0.53> transmit 0.0} finish{ase3}}}
cylinder {< -0.24,  -2.19,  -1.14>, < -1.23,  -2.19,  -1.12>, Rbond texture{pigment {color rgb <1.00, 0.05, 0.05> transmit 0.0} finish{ase3}}}
cylinder {< -2.23,  -2.19,  -1.11>, < -2.23,  -1.46,  -0.55>, Rbond texture{pigment {color rgb <0.09, 0.33, 0.53> transmit 0.0} finish{ase3}}}
cylinder {< -2.23,  -0.73,  -0.00>, < -2.23,  -1.46,  -0.55>, Rbond texture{pigment {color rgb <1.00, 0.05, 0.05> transmit 0.0} finish{ase3}}}
cylinder {<  0.93,   2.19,  -1.43>, <  0.93,   2.19,  -2.35>, Rbond texture{pigment {color rgb <0.09, 0.33, 0.53> transmit 0.0} finish{ase3}}}
cylinder {<  0.93,   2.19,  -3.27>, <  0.93,   2.19,  -2.35>, Rbond texture{pigment {color rgb <1.00, 0.05, 0.05> transmit 0.0} finish{ase3}}}
cylinder {<  0.93,   2.19,  -1.43>, <  0.35,   1.46,  -1.28>, Rbond texture{pigment {color rgb <0.09, 0.33, 0.53> transmit 0.0} finish{ase3}}}
cylinder {< -0.24,   0.73,  -1.14>, <  0.35,   1.46,  -1.28>, Rbond texture{pigment {color rgb <1.00, 0.05, 0.05> transmit 0.0} finish{ase3}}}
cylinder {<  0.93,   2.19,  -1.43>, <  1.52,   1.46,  -1.28>, Rbond texture{pigment {color rgb <0.09, 0.33, 0.53> transmit 0.0} finish{ase3}}}
cylinder {<  2.11,   0.73,  -1.14>, <  1.52,   1.46,  -1.28>, Rbond texture{pigment {color rgb <1.00, 0.05, 0.05> transmit 0.0} finish{ase3}}}
cylinder {<  0.93,  -0.73,  -1.43>, <  0.93,  -0.73,  -2.35>, Rbond texture{pigment {color rgb <0.40, 0.56, 0.56> transmit 0.0} finish{ase3}}}
cylinder {<  0.93,  -0.73,  -3.27>, <  0.93,  -0.73,  -2.35>, Rbond texture{pigment {color rgb <1.00, 0.05, 0.05> transmit 0.0} finish{ase3}}}
cylinder {<  0.93,  -0.73,  -1.43>, <  0.35,   0.00,  -1.28>, Rbond texture{pigment {color rgb <0.40, 0.56, 0.56> transmit 0.0} finish{ase3}}}
cylinder {< -0.24,   0.73,  -1.14>, <  0.35,   0.00,  -1.28>, Rbond texture{pigment {color rgb <1.00, 0.05, 0.05> transmit 0.0} finish{ase3}}}
cylinder {<  0.93,  -0.73,  -1.43>, <  0.35,  -1.46,  -1.28>, Rbond texture{pigment {color rgb <0.40, 0.56, 0.56> transmit 0.0} finish{ase3}}}
cylinder {< -0.24,  -2.19,  -1.14>, <  0.35,  -1.46,  -1.28>, Rbond texture{pigment {color rgb <1.00, 0.05, 0.05> transmit 0.0} finish{ase3}}}
cylinder {<  0.93,  -0.73,  -1.43>, <  1.52,   0.00,  -1.28>, Rbond texture{pigment {color rgb <0.40, 0.56, 0.56> transmit 0.0} finish{ase3}}}
cylinder {<  2.11,   0.73,  -1.14>, <  1.52,   0.00,  -1.28>, Rbond texture{pigment {color rgb <1.00, 0.05, 0.05> transmit 0.0} finish{ase3}}}
cylinder {<  0.93,  -0.73,  -1.43>, <  1.52,  -1.46,  -1.28>, Rbond texture{pigment {color rgb <0.40, 0.56, 0.56> transmit 0.0} finish{ase3}}}
cylinder {<  2.11,  -2.19,  -1.14>, <  1.52,  -1.46,  -1.28>, Rbond texture{pigment {color rgb <1.00, 0.05, 0.05> transmit 0.0} finish{ase3}}}
