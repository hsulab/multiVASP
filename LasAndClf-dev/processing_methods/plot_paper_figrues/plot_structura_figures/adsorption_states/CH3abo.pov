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

atom(< -0.14,  -0.73,  -0.06>, 0.26, rgb <1.00, 1.00, 1.00>, 0.0, ase3) // #0 
atom(<  1.44,  -1.63,  -0.00>, 0.26, rgb <1.00, 1.00, 1.00>, 0.0, ase3) // #1 
atom(<  1.44,   0.17,   0.00>, 0.26, rgb <1.00, 1.00, 1.00>, 0.0, ase3) // #2 
atom(<  0.92,  -0.73,  -0.35>, 0.65, rgb <0.56, 0.56, 0.56>, 0.0, ase3) // #3 
atom(<  0.93,   2.19, -13.36>, 0.56, rgb <1.00, 0.05, 0.05>, 0.0, ase3) // #4 
atom(<  0.93,  -0.73, -13.36>, 0.56, rgb <1.00, 0.05, 0.05>, 0.0, ase3) // #5 
atom(< -1.00,   0.73, -12.14>, 0.56, rgb <1.00, 0.05, 0.05>, 0.0, ase3) // #6 
atom(< -1.00,  -2.19, -12.14>, 0.56, rgb <1.00, 0.05, 0.05>, 0.0, ase3) // #7 
atom(<  2.87,   0.73, -12.14>, 0.56, rgb <1.00, 0.05, 0.05>, 0.0, ase3) // #8 
atom(<  2.87,  -2.19, -12.14>, 0.56, rgb <1.00, 0.05, 0.05>, 0.0, ase3) // #9 
atom(<  0.93,   2.19, -10.91>, 0.56, rgb <1.00, 0.05, 0.05>, 0.0, ase3) // #10 
atom(<  0.93,  -0.73, -10.91>, 0.56, rgb <1.00, 0.05, 0.05>, 0.0, ase3) // #11 
atom(< -2.23,   2.19, -10.20>, 0.56, rgb <1.00, 0.05, 0.05>, 0.0, ase3) // #12 
atom(< -2.23,  -0.73, -10.20>, 0.56, rgb <1.00, 0.05, 0.05>, 0.0, ase3) // #13 
atom(< -0.29,   0.73,  -8.98>, 0.56, rgb <1.00, 0.05, 0.05>, 0.0, ase3) // #14 
atom(< -0.29,  -2.19,  -8.98>, 0.56, rgb <1.00, 0.05, 0.05>, 0.0, ase3) // #15 
atom(<  2.16,   0.73,  -8.98>, 0.56, rgb <1.00, 0.05, 0.05>, 0.0, ase3) // #16 
atom(<  2.16,  -2.19,  -8.98>, 0.56, rgb <1.00, 0.05, 0.05>, 0.0, ase3) // #17 
atom(< -2.23,   2.19,  -7.75>, 0.56, rgb <1.00, 0.05, 0.05>, 0.0, ase3) // #18 
atom(< -2.23,  -0.73,  -7.75>, 0.56, rgb <1.00, 0.05, 0.05>, 0.0, ase3) // #19 
atom(<  0.94,   2.19,  -7.05>, 0.56, rgb <1.00, 0.05, 0.05>, 0.0, ase3) // #20 
atom(<  0.94,  -0.73,  -7.08>, 0.56, rgb <1.00, 0.05, 0.05>, 0.0, ase3) // #21 
atom(< -1.00,   0.73,  -5.82>, 0.56, rgb <1.00, 0.05, 0.05>, 0.0, ase3) // #22 
atom(< -1.00,  -2.19,  -5.82>, 0.56, rgb <1.00, 0.05, 0.05>, 0.0, ase3) // #23 
atom(<  2.86,   0.73,  -5.81>, 0.56, rgb <1.00, 0.05, 0.05>, 0.0, ase3) // #24 
atom(<  2.86,  -2.19,  -5.81>, 0.56, rgb <1.00, 0.05, 0.05>, 0.0, ase3) // #25 
atom(<  0.92,   2.19,  -4.64>, 0.56, rgb <1.00, 0.05, 0.05>, 0.0, ase3) // #26 
atom(<  0.93,  -0.73,  -4.61>, 0.56, rgb <1.00, 0.05, 0.05>, 0.0, ase3) // #27 
atom(< -2.21,   2.19,  -3.84>, 0.56, rgb <1.00, 0.05, 0.05>, 0.0, ase3) // #28 
atom(< -2.21,  -0.73,  -3.84>, 0.56, rgb <1.00, 0.05, 0.05>, 0.0, ase3) // #29 
atom(< -0.26,   0.80,  -2.47>, 0.56, rgb <1.00, 0.05, 0.05>, 0.0, ase3) // #30 
atom(< -0.26,  -2.26,  -2.47>, 0.56, rgb <1.00, 0.05, 0.05>, 0.0, ase3) // #31 
atom(<  2.14,   0.80,  -2.51>, 0.56, rgb <1.00, 0.05, 0.05>, 0.0, ase3) // #32 
atom(<  2.14,  -2.26,  -2.52>, 0.56, rgb <1.00, 0.05, 0.05>, 0.0, ase3) // #33 
atom(< -2.23,  -0.73,  -1.37>, 0.56, rgb <1.00, 0.05, 0.05>, 0.0, ase3) // #34 
atom(< -2.23,   2.19,  -1.35>, 0.56, rgb <1.00, 0.05, 0.05>, 0.0, ase3) // #35 
atom(< -2.23,   2.19, -12.14>, 1.20, rgb <0.09, 0.33, 0.53>, 0.0, ase3) // #36 
atom(< -2.23,  -0.73, -12.14>, 1.20, rgb <0.09, 0.33, 0.53>, 0.0, ase3) // #37 
atom(<  0.93,   0.73, -12.14>, 1.20, rgb <0.09, 0.33, 0.53>, 0.0, ase3) // #38 
atom(<  0.93,  -2.19, -12.14>, 1.20, rgb <0.09, 0.33, 0.53>, 0.0, ase3) // #39 
atom(< -2.23,   0.73,  -8.98>, 1.20, rgb <0.09, 0.33, 0.53>, 0.0, ase3) // #40 
atom(< -2.23,  -2.19,  -8.98>, 1.20, rgb <0.09, 0.33, 0.53>, 0.0, ase3) // #41 
atom(<  0.93,   2.19,  -8.98>, 1.20, rgb <0.09, 0.33, 0.53>, 0.0, ase3) // #42 
atom(<  0.93,  -0.73,  -8.98>, 1.20, rgb <0.09, 0.33, 0.53>, 0.0, ase3) // #43 
atom(<  0.93,  -2.16,  -5.86>, 1.20, rgb <0.09, 0.33, 0.53>, 0.0, ase3) // #44 
atom(<  0.93,   0.70,  -5.86>, 1.20, rgb <0.09, 0.33, 0.53>, 0.0, ase3) // #45 
atom(< -2.22,   2.19,  -5.78>, 1.20, rgb <0.09, 0.33, 0.53>, 0.0, ase3) // #46 
atom(< -2.23,  -0.73,  -5.76>, 1.20, rgb <0.09, 0.33, 0.53>, 0.0, ase3) // #47 
atom(<  0.94,   2.19,  -2.84>, 1.20, rgb <0.09, 0.33, 0.53>, 0.0, ase3) // #48 
atom(< -2.22,  -2.19,  -2.50>, 1.20, rgb <0.09, 0.33, 0.53>, 0.0, ase3) // #49 
atom(< -2.22,   0.73,  -2.50>, 1.20, rgb <0.09, 0.33, 0.53>, 0.0, ase3) // #50 
atom(<  0.94,  -0.73,  -2.40>, 1.02, rgb <0.40, 0.56, 0.56>, 0.0, ase3) // #51 
cylinder {<  0.92,  -0.73,  -0.35>, <  0.39,  -0.73,  -0.21>, Rbond texture{pigment {color rgb <0.56, 0.56, 0.56> transmit 0.0} finish{ase3}}}
cylinder {< -0.14,  -0.73,  -0.06>, <  0.39,  -0.73,  -0.21>, Rbond texture{pigment {color rgb <1.00, 1.00, 1.00> transmit 0.0} finish{ase3}}}
cylinder {<  0.92,  -0.73,  -0.35>, <  1.18,  -1.18,  -0.18>, Rbond texture{pigment {color rgb <0.56, 0.56, 0.56> transmit 0.0} finish{ase3}}}
cylinder {<  1.44,  -1.63,  -0.00>, <  1.18,  -1.18,  -0.18>, Rbond texture{pigment {color rgb <1.00, 1.00, 1.00> transmit 0.0} finish{ase3}}}
cylinder {<  0.92,  -0.73,  -0.35>, <  1.18,  -0.28,  -0.18>, Rbond texture{pigment {color rgb <0.56, 0.56, 0.56> transmit 0.0} finish{ase3}}}
cylinder {<  1.44,   0.17,   0.00>, <  1.18,  -0.28,  -0.18>, Rbond texture{pigment {color rgb <1.00, 1.00, 1.00> transmit 0.0} finish{ase3}}}
cylinder {< -2.23,   2.19, -12.14>, < -1.62,   1.46, -12.14>, Rbond texture{pigment {color rgb <0.09, 0.33, 0.53> transmit 0.0} finish{ase3}}}
cylinder {< -1.00,   0.73, -12.14>, < -1.62,   1.46, -12.14>, Rbond texture{pigment {color rgb <1.00, 0.05, 0.05> transmit 0.0} finish{ase3}}}
cylinder {< -2.23,   2.19, -12.14>, < -2.23,   2.19, -11.17>, Rbond texture{pigment {color rgb <0.09, 0.33, 0.53> transmit 0.0} finish{ase3}}}
cylinder {< -2.23,   2.19, -10.20>, < -2.23,   2.19, -11.17>, Rbond texture{pigment {color rgb <1.00, 0.05, 0.05> transmit 0.0} finish{ase3}}}
cylinder {< -2.23,  -0.73, -12.14>, < -1.62,   0.00, -12.14>, Rbond texture{pigment {color rgb <0.09, 0.33, 0.53> transmit 0.0} finish{ase3}}}
cylinder {< -1.00,   0.73, -12.14>, < -1.62,   0.00, -12.14>, Rbond texture{pigment {color rgb <1.00, 0.05, 0.05> transmit 0.0} finish{ase3}}}
cylinder {< -2.23,  -0.73, -12.14>, < -1.62,  -1.46, -12.14>, Rbond texture{pigment {color rgb <0.09, 0.33, 0.53> transmit 0.0} finish{ase3}}}
cylinder {< -1.00,  -2.19, -12.14>, < -1.62,  -1.46, -12.14>, Rbond texture{pigment {color rgb <1.00, 0.05, 0.05> transmit 0.0} finish{ase3}}}
cylinder {< -2.23,  -0.73, -12.14>, < -2.23,  -0.73, -11.17>, Rbond texture{pigment {color rgb <0.09, 0.33, 0.53> transmit 0.0} finish{ase3}}}
cylinder {< -2.23,  -0.73, -10.20>, < -2.23,  -0.73, -11.17>, Rbond texture{pigment {color rgb <1.00, 0.05, 0.05> transmit 0.0} finish{ase3}}}
cylinder {<  0.93,   0.73, -12.14>, <  0.93,   1.46, -12.75>, Rbond texture{pigment {color rgb <0.09, 0.33, 0.53> transmit 0.0} finish{ase3}}}
cylinder {<  0.93,   2.19, -13.36>, <  0.93,   1.46, -12.75>, Rbond texture{pigment {color rgb <1.00, 0.05, 0.05> transmit 0.0} finish{ase3}}}
cylinder {<  0.93,   0.73, -12.14>, <  0.93,   0.00, -12.75>, Rbond texture{pigment {color rgb <0.09, 0.33, 0.53> transmit 0.0} finish{ase3}}}
cylinder {<  0.93,  -0.73, -13.36>, <  0.93,   0.00, -12.75>, Rbond texture{pigment {color rgb <1.00, 0.05, 0.05> transmit 0.0} finish{ase3}}}
cylinder {<  0.93,   0.73, -12.14>, < -0.04,   0.73, -12.14>, Rbond texture{pigment {color rgb <0.09, 0.33, 0.53> transmit 0.0} finish{ase3}}}
cylinder {< -1.00,   0.73, -12.14>, < -0.04,   0.73, -12.14>, Rbond texture{pigment {color rgb <1.00, 0.05, 0.05> transmit 0.0} finish{ase3}}}
cylinder {<  0.93,   0.73, -12.14>, <  1.90,   0.73, -12.14>, Rbond texture{pigment {color rgb <0.09, 0.33, 0.53> transmit 0.0} finish{ase3}}}
cylinder {<  2.87,   0.73, -12.14>, <  1.90,   0.73, -12.14>, Rbond texture{pigment {color rgb <1.00, 0.05, 0.05> transmit 0.0} finish{ase3}}}
cylinder {<  0.93,   0.73, -12.14>, <  0.93,   1.46, -11.52>, Rbond texture{pigment {color rgb <0.09, 0.33, 0.53> transmit 0.0} finish{ase3}}}
cylinder {<  0.93,   2.19, -10.91>, <  0.93,   1.46, -11.52>, Rbond texture{pigment {color rgb <1.00, 0.05, 0.05> transmit 0.0} finish{ase3}}}
cylinder {<  0.93,   0.73, -12.14>, <  0.93,   0.00, -11.52>, Rbond texture{pigment {color rgb <0.09, 0.33, 0.53> transmit 0.0} finish{ase3}}}
cylinder {<  0.93,  -0.73, -10.91>, <  0.93,   0.00, -11.52>, Rbond texture{pigment {color rgb <1.00, 0.05, 0.05> transmit 0.0} finish{ase3}}}
cylinder {<  0.93,  -2.19, -12.14>, <  0.93,  -1.46, -12.75>, Rbond texture{pigment {color rgb <0.09, 0.33, 0.53> transmit 0.0} finish{ase3}}}
cylinder {<  0.93,  -0.73, -13.36>, <  0.93,  -1.46, -12.75>, Rbond texture{pigment {color rgb <1.00, 0.05, 0.05> transmit 0.0} finish{ase3}}}
cylinder {<  0.93,  -2.19, -12.14>, < -0.04,  -2.19, -12.14>, Rbond texture{pigment {color rgb <0.09, 0.33, 0.53> transmit 0.0} finish{ase3}}}
cylinder {< -1.00,  -2.19, -12.14>, < -0.04,  -2.19, -12.14>, Rbond texture{pigment {color rgb <1.00, 0.05, 0.05> transmit 0.0} finish{ase3}}}
cylinder {<  0.93,  -2.19, -12.14>, <  1.90,  -2.19, -12.14>, Rbond texture{pigment {color rgb <0.09, 0.33, 0.53> transmit 0.0} finish{ase3}}}
cylinder {<  2.87,  -2.19, -12.14>, <  1.90,  -2.19, -12.14>, Rbond texture{pigment {color rgb <1.00, 0.05, 0.05> transmit 0.0} finish{ase3}}}
cylinder {<  0.93,  -2.19, -12.14>, <  0.93,  -1.46, -11.52>, Rbond texture{pigment {color rgb <0.09, 0.33, 0.53> transmit 0.0} finish{ase3}}}
cylinder {<  0.93,  -0.73, -10.91>, <  0.93,  -1.46, -11.52>, Rbond texture{pigment {color rgb <1.00, 0.05, 0.05> transmit 0.0} finish{ase3}}}
cylinder {< -2.23,   0.73,  -8.98>, < -2.23,   1.46,  -9.59>, Rbond texture{pigment {color rgb <0.09, 0.33, 0.53> transmit 0.0} finish{ase3}}}
cylinder {< -2.23,   2.19, -10.20>, < -2.23,   1.46,  -9.59>, Rbond texture{pigment {color rgb <1.00, 0.05, 0.05> transmit 0.0} finish{ase3}}}
cylinder {< -2.23,   0.73,  -8.98>, < -2.23,   0.00,  -9.59>, Rbond texture{pigment {color rgb <0.09, 0.33, 0.53> transmit 0.0} finish{ase3}}}
cylinder {< -2.23,  -0.73, -10.20>, < -2.23,   0.00,  -9.59>, Rbond texture{pigment {color rgb <1.00, 0.05, 0.05> transmit 0.0} finish{ase3}}}
cylinder {< -2.23,   0.73,  -8.98>, < -1.26,   0.73,  -8.98>, Rbond texture{pigment {color rgb <0.09, 0.33, 0.53> transmit 0.0} finish{ase3}}}
cylinder {< -0.29,   0.73,  -8.98>, < -1.26,   0.73,  -8.98>, Rbond texture{pigment {color rgb <1.00, 0.05, 0.05> transmit 0.0} finish{ase3}}}
cylinder {< -2.23,   0.73,  -8.98>, < -2.23,   1.46,  -8.36>, Rbond texture{pigment {color rgb <0.09, 0.33, 0.53> transmit 0.0} finish{ase3}}}
cylinder {< -2.23,   2.19,  -7.75>, < -2.23,   1.46,  -8.36>, Rbond texture{pigment {color rgb <1.00, 0.05, 0.05> transmit 0.0} finish{ase3}}}
cylinder {< -2.23,   0.73,  -8.98>, < -2.23,   0.00,  -8.36>, Rbond texture{pigment {color rgb <0.09, 0.33, 0.53> transmit 0.0} finish{ase3}}}
cylinder {< -2.23,  -0.73,  -7.75>, < -2.23,   0.00,  -8.36>, Rbond texture{pigment {color rgb <1.00, 0.05, 0.05> transmit 0.0} finish{ase3}}}
cylinder {< -2.23,  -2.19,  -8.98>, < -2.23,  -1.46,  -9.59>, Rbond texture{pigment {color rgb <0.09, 0.33, 0.53> transmit 0.0} finish{ase3}}}
cylinder {< -2.23,  -0.73, -10.20>, < -2.23,  -1.46,  -9.59>, Rbond texture{pigment {color rgb <1.00, 0.05, 0.05> transmit 0.0} finish{ase3}}}
cylinder {< -2.23,  -2.19,  -8.98>, < -1.26,  -2.19,  -8.98>, Rbond texture{pigment {color rgb <0.09, 0.33, 0.53> transmit 0.0} finish{ase3}}}
cylinder {< -0.29,  -2.19,  -8.98>, < -1.26,  -2.19,  -8.98>, Rbond texture{pigment {color rgb <1.00, 0.05, 0.05> transmit 0.0} finish{ase3}}}
cylinder {< -2.23,  -2.19,  -8.98>, < -2.23,  -1.46,  -8.36>, Rbond texture{pigment {color rgb <0.09, 0.33, 0.53> transmit 0.0} finish{ase3}}}
cylinder {< -2.23,  -0.73,  -7.75>, < -2.23,  -1.46,  -8.36>, Rbond texture{pigment {color rgb <1.00, 0.05, 0.05> transmit 0.0} finish{ase3}}}
cylinder {<  0.93,   2.19,  -8.98>, <  0.93,   2.19,  -9.94>, Rbond texture{pigment {color rgb <0.09, 0.33, 0.53> transmit 0.0} finish{ase3}}}
cylinder {<  0.93,   2.19, -10.91>, <  0.93,   2.19,  -9.94>, Rbond texture{pigment {color rgb <1.00, 0.05, 0.05> transmit 0.0} finish{ase3}}}
cylinder {<  0.93,   2.19,  -8.98>, <  0.32,   1.46,  -8.98>, Rbond texture{pigment {color rgb <0.09, 0.33, 0.53> transmit 0.0} finish{ase3}}}
cylinder {< -0.29,   0.73,  -8.98>, <  0.32,   1.46,  -8.98>, Rbond texture{pigment {color rgb <1.00, 0.05, 0.05> transmit 0.0} finish{ase3}}}
cylinder {<  0.93,   2.19,  -8.98>, <  1.54,   1.46,  -8.98>, Rbond texture{pigment {color rgb <0.09, 0.33, 0.53> transmit 0.0} finish{ase3}}}
cylinder {<  2.16,   0.73,  -8.98>, <  1.54,   1.46,  -8.98>, Rbond texture{pigment {color rgb <1.00, 0.05, 0.05> transmit 0.0} finish{ase3}}}
cylinder {<  0.93,   2.19,  -8.98>, <  0.93,   2.19,  -8.01>, Rbond texture{pigment {color rgb <0.09, 0.33, 0.53> transmit 0.0} finish{ase3}}}
cylinder {<  0.94,   2.19,  -7.05>, <  0.93,   2.19,  -8.01>, Rbond texture{pigment {color rgb <1.00, 0.05, 0.05> transmit 0.0} finish{ase3}}}
cylinder {<  0.93,  -0.73,  -8.98>, <  0.93,  -0.73,  -9.94>, Rbond texture{pigment {color rgb <0.09, 0.33, 0.53> transmit 0.0} finish{ase3}}}
cylinder {<  0.93,  -0.73, -10.91>, <  0.93,  -0.73,  -9.94>, Rbond texture{pigment {color rgb <1.00, 0.05, 0.05> transmit 0.0} finish{ase3}}}
cylinder {<  0.93,  -0.73,  -8.98>, <  0.32,   0.00,  -8.98>, Rbond texture{pigment {color rgb <0.09, 0.33, 0.53> transmit 0.0} finish{ase3}}}
cylinder {< -0.29,   0.73,  -8.98>, <  0.32,   0.00,  -8.98>, Rbond texture{pigment {color rgb <1.00, 0.05, 0.05> transmit 0.0} finish{ase3}}}
cylinder {<  0.93,  -0.73,  -8.98>, <  0.32,  -1.46,  -8.98>, Rbond texture{pigment {color rgb <0.09, 0.33, 0.53> transmit 0.0} finish{ase3}}}
cylinder {< -0.29,  -2.19,  -8.98>, <  0.32,  -1.46,  -8.98>, Rbond texture{pigment {color rgb <1.00, 0.05, 0.05> transmit 0.0} finish{ase3}}}
cylinder {<  0.93,  -0.73,  -8.98>, <  1.54,   0.00,  -8.98>, Rbond texture{pigment {color rgb <0.09, 0.33, 0.53> transmit 0.0} finish{ase3}}}
cylinder {<  2.16,   0.73,  -8.98>, <  1.54,   0.00,  -8.98>, Rbond texture{pigment {color rgb <1.00, 0.05, 0.05> transmit 0.0} finish{ase3}}}
cylinder {<  0.93,  -0.73,  -8.98>, <  1.54,  -1.46,  -8.98>, Rbond texture{pigment {color rgb <0.09, 0.33, 0.53> transmit 0.0} finish{ase3}}}
cylinder {<  2.16,  -2.19,  -8.98>, <  1.54,  -1.46,  -8.98>, Rbond texture{pigment {color rgb <1.00, 0.05, 0.05> transmit 0.0} finish{ase3}}}
cylinder {<  0.93,  -0.73,  -8.98>, <  0.93,  -0.73,  -8.03>, Rbond texture{pigment {color rgb <0.09, 0.33, 0.53> transmit 0.0} finish{ase3}}}
cylinder {<  0.94,  -0.73,  -7.08>, <  0.93,  -0.73,  -8.03>, Rbond texture{pigment {color rgb <1.00, 0.05, 0.05> transmit 0.0} finish{ase3}}}
cylinder {<  0.93,  -2.16,  -5.86>, <  0.93,  -1.45,  -6.47>, Rbond texture{pigment {color rgb <0.09, 0.33, 0.53> transmit 0.0} finish{ase3}}}
cylinder {<  0.94,  -0.73,  -7.08>, <  0.93,  -1.45,  -6.47>, Rbond texture{pigment {color rgb <1.00, 0.05, 0.05> transmit 0.0} finish{ase3}}}
cylinder {<  0.93,  -2.16,  -5.86>, < -0.03,  -2.18,  -5.84>, Rbond texture{pigment {color rgb <0.09, 0.33, 0.53> transmit 0.0} finish{ase3}}}
cylinder {< -1.00,  -2.19,  -5.82>, < -0.03,  -2.18,  -5.84>, Rbond texture{pigment {color rgb <1.00, 0.05, 0.05> transmit 0.0} finish{ase3}}}
cylinder {<  0.93,  -2.16,  -5.86>, <  1.90,  -2.18,  -5.83>, Rbond texture{pigment {color rgb <0.09, 0.33, 0.53> transmit 0.0} finish{ase3}}}
cylinder {<  2.86,  -2.19,  -5.81>, <  1.90,  -2.18,  -5.83>, Rbond texture{pigment {color rgb <1.00, 0.05, 0.05> transmit 0.0} finish{ase3}}}
cylinder {<  0.93,  -2.16,  -5.86>, <  0.93,  -1.45,  -5.24>, Rbond texture{pigment {color rgb <0.09, 0.33, 0.53> transmit 0.0} finish{ase3}}}
cylinder {<  0.93,  -0.73,  -4.61>, <  0.93,  -1.45,  -5.24>, Rbond texture{pigment {color rgb <1.00, 0.05, 0.05> transmit 0.0} finish{ase3}}}
cylinder {<  0.93,   0.70,  -5.86>, <  0.93,   1.45,  -6.45>, Rbond texture{pigment {color rgb <0.09, 0.33, 0.53> transmit 0.0} finish{ase3}}}
cylinder {<  0.94,   2.19,  -7.05>, <  0.93,   1.45,  -6.45>, Rbond texture{pigment {color rgb <1.00, 0.05, 0.05> transmit 0.0} finish{ase3}}}
cylinder {<  0.93,   0.70,  -5.86>, <  0.93,  -0.01,  -6.47>, Rbond texture{pigment {color rgb <0.09, 0.33, 0.53> transmit 0.0} finish{ase3}}}
cylinder {<  0.94,  -0.73,  -7.08>, <  0.93,  -0.01,  -6.47>, Rbond texture{pigment {color rgb <1.00, 0.05, 0.05> transmit 0.0} finish{ase3}}}
cylinder {<  0.93,   0.70,  -5.86>, < -0.03,   0.72,  -5.84>, Rbond texture{pigment {color rgb <0.09, 0.33, 0.53> transmit 0.0} finish{ase3}}}
cylinder {< -1.00,   0.73,  -5.82>, < -0.03,   0.72,  -5.84>, Rbond texture{pigment {color rgb <1.00, 0.05, 0.05> transmit 0.0} finish{ase3}}}
cylinder {<  0.93,   0.70,  -5.86>, <  1.90,   0.72,  -5.83>, Rbond texture{pigment {color rgb <0.09, 0.33, 0.53> transmit 0.0} finish{ase3}}}
cylinder {<  2.86,   0.73,  -5.81>, <  1.90,   0.72,  -5.83>, Rbond texture{pigment {color rgb <1.00, 0.05, 0.05> transmit 0.0} finish{ase3}}}
cylinder {<  0.93,   0.70,  -5.86>, <  0.93,   1.45,  -5.25>, Rbond texture{pigment {color rgb <0.09, 0.33, 0.53> transmit 0.0} finish{ase3}}}
cylinder {<  0.92,   2.19,  -4.64>, <  0.93,   1.45,  -5.25>, Rbond texture{pigment {color rgb <1.00, 0.05, 0.05> transmit 0.0} finish{ase3}}}
cylinder {<  0.93,   0.70,  -5.86>, <  0.93,  -0.01,  -5.24>, Rbond texture{pigment {color rgb <0.09, 0.33, 0.53> transmit 0.0} finish{ase3}}}
cylinder {<  0.93,  -0.73,  -4.61>, <  0.93,  -0.01,  -5.24>, Rbond texture{pigment {color rgb <1.00, 0.05, 0.05> transmit 0.0} finish{ase3}}}
cylinder {< -2.22,   2.19,  -5.78>, < -2.23,   2.19,  -6.76>, Rbond texture{pigment {color rgb <0.09, 0.33, 0.53> transmit 0.0} finish{ase3}}}
cylinder {< -2.23,   2.19,  -7.75>, < -2.23,   2.19,  -6.76>, Rbond texture{pigment {color rgb <1.00, 0.05, 0.05> transmit 0.0} finish{ase3}}}
cylinder {< -2.22,   2.19,  -5.78>, < -1.61,   1.46,  -5.80>, Rbond texture{pigment {color rgb <0.09, 0.33, 0.53> transmit 0.0} finish{ase3}}}
cylinder {< -1.00,   0.73,  -5.82>, < -1.61,   1.46,  -5.80>, Rbond texture{pigment {color rgb <1.00, 0.05, 0.05> transmit 0.0} finish{ase3}}}
cylinder {< -2.22,   2.19,  -5.78>, < -2.22,   2.19,  -4.81>, Rbond texture{pigment {color rgb <0.09, 0.33, 0.53> transmit 0.0} finish{ase3}}}
cylinder {< -2.21,   2.19,  -3.84>, < -2.22,   2.19,  -4.81>, Rbond texture{pigment {color rgb <1.00, 0.05, 0.05> transmit 0.0} finish{ase3}}}
cylinder {< -2.23,  -0.73,  -5.76>, < -2.23,  -0.73,  -6.76>, Rbond texture{pigment {color rgb <0.09, 0.33, 0.53> transmit 0.0} finish{ase3}}}
cylinder {< -2.23,  -0.73,  -7.75>, < -2.23,  -0.73,  -6.76>, Rbond texture{pigment {color rgb <1.00, 0.05, 0.05> transmit 0.0} finish{ase3}}}
cylinder {< -2.23,  -0.73,  -5.76>, < -1.61,   0.00,  -5.79>, Rbond texture{pigment {color rgb <0.09, 0.33, 0.53> transmit 0.0} finish{ase3}}}
cylinder {< -1.00,   0.73,  -5.82>, < -1.61,   0.00,  -5.79>, Rbond texture{pigment {color rgb <1.00, 0.05, 0.05> transmit 0.0} finish{ase3}}}
cylinder {< -2.23,  -0.73,  -5.76>, < -1.61,  -1.46,  -5.79>, Rbond texture{pigment {color rgb <0.09, 0.33, 0.53> transmit 0.0} finish{ase3}}}
cylinder {< -1.00,  -2.19,  -5.82>, < -1.61,  -1.46,  -5.79>, Rbond texture{pigment {color rgb <1.00, 0.05, 0.05> transmit 0.0} finish{ase3}}}
cylinder {< -2.23,  -0.73,  -5.76>, < -2.22,  -0.73,  -4.80>, Rbond texture{pigment {color rgb <0.09, 0.33, 0.53> transmit 0.0} finish{ase3}}}
cylinder {< -2.21,  -0.73,  -3.84>, < -2.22,  -0.73,  -4.80>, Rbond texture{pigment {color rgb <1.00, 0.05, 0.05> transmit 0.0} finish{ase3}}}
cylinder {<  0.94,   2.19,  -2.84>, <  0.93,   2.19,  -3.74>, Rbond texture{pigment {color rgb <0.09, 0.33, 0.53> transmit 0.0} finish{ase3}}}
cylinder {<  0.92,   2.19,  -4.64>, <  0.93,   2.19,  -3.74>, Rbond texture{pigment {color rgb <1.00, 0.05, 0.05> transmit 0.0} finish{ase3}}}
cylinder {<  0.94,   2.19,  -2.84>, <  0.34,   1.49,  -2.66>, Rbond texture{pigment {color rgb <0.09, 0.33, 0.53> transmit 0.0} finish{ase3}}}
cylinder {< -0.26,   0.80,  -2.47>, <  0.34,   1.49,  -2.66>, Rbond texture{pigment {color rgb <1.00, 0.05, 0.05> transmit 0.0} finish{ase3}}}
cylinder {<  0.94,   2.19,  -2.84>, <  1.54,   1.49,  -2.68>, Rbond texture{pigment {color rgb <0.09, 0.33, 0.53> transmit 0.0} finish{ase3}}}
cylinder {<  2.14,   0.80,  -2.51>, <  1.54,   1.49,  -2.68>, Rbond texture{pigment {color rgb <1.00, 0.05, 0.05> transmit 0.0} finish{ase3}}}
cylinder {< -2.22,  -2.19,  -2.50>, < -2.22,  -1.46,  -3.17>, Rbond texture{pigment {color rgb <0.09, 0.33, 0.53> transmit 0.0} finish{ase3}}}
cylinder {< -2.21,  -0.73,  -3.84>, < -2.22,  -1.46,  -3.17>, Rbond texture{pigment {color rgb <1.00, 0.05, 0.05> transmit 0.0} finish{ase3}}}
cylinder {< -2.22,  -2.19,  -2.50>, < -1.24,  -2.23,  -2.49>, Rbond texture{pigment {color rgb <0.09, 0.33, 0.53> transmit 0.0} finish{ase3}}}
cylinder {< -0.26,  -2.26,  -2.47>, < -1.24,  -2.23,  -2.49>, Rbond texture{pigment {color rgb <1.00, 0.05, 0.05> transmit 0.0} finish{ase3}}}
cylinder {< -2.22,  -2.19,  -2.50>, < -2.23,  -1.46,  -1.93>, Rbond texture{pigment {color rgb <0.09, 0.33, 0.53> transmit 0.0} finish{ase3}}}
cylinder {< -2.23,  -0.73,  -1.37>, < -2.23,  -1.46,  -1.93>, Rbond texture{pigment {color rgb <1.00, 0.05, 0.05> transmit 0.0} finish{ase3}}}
cylinder {< -2.22,   0.73,  -2.50>, < -2.21,   1.46,  -3.17>, Rbond texture{pigment {color rgb <0.09, 0.33, 0.53> transmit 0.0} finish{ase3}}}
cylinder {< -2.21,   2.19,  -3.84>, < -2.21,   1.46,  -3.17>, Rbond texture{pigment {color rgb <1.00, 0.05, 0.05> transmit 0.0} finish{ase3}}}
cylinder {< -2.22,   0.73,  -2.50>, < -2.22,   0.00,  -3.17>, Rbond texture{pigment {color rgb <0.09, 0.33, 0.53> transmit 0.0} finish{ase3}}}
cylinder {< -2.21,  -0.73,  -3.84>, < -2.22,   0.00,  -3.17>, Rbond texture{pigment {color rgb <1.00, 0.05, 0.05> transmit 0.0} finish{ase3}}}
cylinder {< -2.22,   0.73,  -2.50>, < -1.24,   0.77,  -2.49>, Rbond texture{pigment {color rgb <0.09, 0.33, 0.53> transmit 0.0} finish{ase3}}}
cylinder {< -0.26,   0.80,  -2.47>, < -1.24,   0.77,  -2.49>, Rbond texture{pigment {color rgb <1.00, 0.05, 0.05> transmit 0.0} finish{ase3}}}
cylinder {< -2.22,   0.73,  -2.50>, < -2.23,   0.00,  -1.93>, Rbond texture{pigment {color rgb <0.09, 0.33, 0.53> transmit 0.0} finish{ase3}}}
cylinder {< -2.23,  -0.73,  -1.37>, < -2.23,   0.00,  -1.93>, Rbond texture{pigment {color rgb <1.00, 0.05, 0.05> transmit 0.0} finish{ase3}}}
cylinder {< -2.22,   0.73,  -2.50>, < -2.23,   1.46,  -1.92>, Rbond texture{pigment {color rgb <0.09, 0.33, 0.53> transmit 0.0} finish{ase3}}}
cylinder {< -2.23,   2.19,  -1.35>, < -2.23,   1.46,  -1.92>, Rbond texture{pigment {color rgb <1.00, 0.05, 0.05> transmit 0.0} finish{ase3}}}
cylinder {<  0.94,  -0.73,  -2.40>, <  0.93,  -0.73,  -1.38>, Rbond texture{pigment {color rgb <0.40, 0.56, 0.56> transmit 0.0} finish{ase3}}}
cylinder {<  0.92,  -0.73,  -0.35>, <  0.93,  -0.73,  -1.38>, Rbond texture{pigment {color rgb <0.56, 0.56, 0.56> transmit 0.0} finish{ase3}}}
cylinder {<  0.94,  -0.73,  -2.40>, <  0.94,  -0.73,  -3.51>, Rbond texture{pigment {color rgb <0.40, 0.56, 0.56> transmit 0.0} finish{ase3}}}
cylinder {<  0.93,  -0.73,  -4.61>, <  0.94,  -0.73,  -3.51>, Rbond texture{pigment {color rgb <1.00, 0.05, 0.05> transmit 0.0} finish{ase3}}}
cylinder {<  0.94,  -0.73,  -2.40>, <  0.34,   0.03,  -2.44>, Rbond texture{pigment {color rgb <0.40, 0.56, 0.56> transmit 0.0} finish{ase3}}}
cylinder {< -0.26,   0.80,  -2.47>, <  0.34,   0.03,  -2.44>, Rbond texture{pigment {color rgb <1.00, 0.05, 0.05> transmit 0.0} finish{ase3}}}
cylinder {<  0.94,  -0.73,  -2.40>, <  0.34,  -1.50,  -2.44>, Rbond texture{pigment {color rgb <0.40, 0.56, 0.56> transmit 0.0} finish{ase3}}}
cylinder {< -0.26,  -2.26,  -2.47>, <  0.34,  -1.50,  -2.44>, Rbond texture{pigment {color rgb <1.00, 0.05, 0.05> transmit 0.0} finish{ase3}}}
cylinder {<  0.94,  -0.73,  -2.40>, <  1.54,   0.03,  -2.46>, Rbond texture{pigment {color rgb <0.40, 0.56, 0.56> transmit 0.0} finish{ase3}}}
cylinder {<  2.14,   0.80,  -2.51>, <  1.54,   0.03,  -2.46>, Rbond texture{pigment {color rgb <1.00, 0.05, 0.05> transmit 0.0} finish{ase3}}}
cylinder {<  0.94,  -0.73,  -2.40>, <  1.54,  -1.50,  -2.46>, Rbond texture{pigment {color rgb <0.40, 0.56, 0.56> transmit 0.0} finish{ase3}}}
cylinder {<  2.14,  -2.26,  -2.52>, <  1.54,  -1.50,  -2.46>, Rbond texture{pigment {color rgb <1.00, 0.05, 0.05> transmit 0.0} finish{ase3}}}
