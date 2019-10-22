#include "colors.inc"
#include "finish.inc"

global_settings {assumed_gamma 1 max_trace_level 6}
background {color White}
camera {perspective
  right -7.11*x up 5.02*y
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

atom(< -1.31,   1.17,  -1.47>, 0.26, rgb <1.00, 1.00, 1.00>, 0.0, ase3) // #0 
atom(<  2.83,  -0.06,  -2.69>, 0.56, rgb <1.00, 0.05, 0.05>, 0.0, ase3) // #1 
atom(<  2.05,  -1.40,   0.00>, 0.56, rgb <1.00, 0.05, 0.05>, 0.0, ase3) // #2 
atom(<  0.45,   0.14,  -3.27>, 0.56, rgb <1.00, 0.05, 0.05>, 0.0, ase3) // #3 
atom(< -0.33,  -1.20,  -0.59>, 0.56, rgb <1.00, 0.05, 0.05>, 0.0, ase3) // #4 
atom(< -1.15,   1.83,  -4.48>, 0.56, rgb <1.00, 0.05, 0.05>, 0.0, ase3) // #5 
atom(< -1.95,   0.60,  -1.94>, 0.56, rgb <1.00, 0.05, 0.05>, 0.0, ase3) // #6 
atom(<  1.99,   0.36,  -4.30>, 1.20, rgb <0.09, 0.33, 0.53>, 0.0, ase3) // #7 
atom(< -1.42,   0.14,  -3.80>, 1.20, rgb <0.09, 0.33, 0.53>, 0.0, ase3) // #8 
atom(< -2.19,  -1.19,  -1.14>, 1.20, rgb <0.09, 0.33, 0.53>, 0.0, ase3) // #9 
atom(<  1.26,  -0.78,  -1.71>, 1.02, rgb <0.40, 0.56, 0.56>, 0.0, ase3) // #10 
cylinder {< -1.95,   0.60,  -1.94>, < -1.63,   0.89,  -1.71>, Rbond texture{pigment {color rgb <1.00, 0.05, 0.05> transmit 0.0} finish{ase3}}}
cylinder {< -1.31,   1.17,  -1.47>, < -1.63,   0.89,  -1.71>, Rbond texture{pigment {color rgb <1.00, 1.00, 1.00> transmit 0.0} finish{ase3}}}
cylinder {<  1.99,   0.36,  -4.30>, <  2.41,   0.15,  -3.50>, Rbond texture{pigment {color rgb <0.09, 0.33, 0.53> transmit 0.0} finish{ase3}}}
cylinder {<  2.83,  -0.06,  -2.69>, <  2.41,   0.15,  -3.50>, Rbond texture{pigment {color rgb <1.00, 0.05, 0.05> transmit 0.0} finish{ase3}}}
cylinder {<  1.99,   0.36,  -4.30>, <  1.22,   0.25,  -3.79>, Rbond texture{pigment {color rgb <0.09, 0.33, 0.53> transmit 0.0} finish{ase3}}}
cylinder {<  0.45,   0.14,  -3.27>, <  1.22,   0.25,  -3.79>, Rbond texture{pigment {color rgb <1.00, 0.05, 0.05> transmit 0.0} finish{ase3}}}
cylinder {< -1.42,   0.14,  -3.80>, < -0.49,   0.14,  -3.53>, Rbond texture{pigment {color rgb <0.09, 0.33, 0.53> transmit 0.0} finish{ase3}}}
cylinder {<  0.45,   0.14,  -3.27>, < -0.49,   0.14,  -3.53>, Rbond texture{pigment {color rgb <1.00, 0.05, 0.05> transmit 0.0} finish{ase3}}}
cylinder {< -1.42,   0.14,  -3.80>, < -1.28,   0.98,  -4.14>, Rbond texture{pigment {color rgb <0.09, 0.33, 0.53> transmit 0.0} finish{ase3}}}
cylinder {< -1.15,   1.83,  -4.48>, < -1.28,   0.98,  -4.14>, Rbond texture{pigment {color rgb <1.00, 0.05, 0.05> transmit 0.0} finish{ase3}}}
cylinder {< -1.42,   0.14,  -3.80>, < -1.68,   0.37,  -2.87>, Rbond texture{pigment {color rgb <0.09, 0.33, 0.53> transmit 0.0} finish{ase3}}}
cylinder {< -1.95,   0.60,  -1.94>, < -1.68,   0.37,  -2.87>, Rbond texture{pigment {color rgb <1.00, 0.05, 0.05> transmit 0.0} finish{ase3}}}
cylinder {< -2.19,  -1.19,  -1.14>, < -1.26,  -1.19,  -0.87>, Rbond texture{pigment {color rgb <0.09, 0.33, 0.53> transmit 0.0} finish{ase3}}}
cylinder {< -0.33,  -1.20,  -0.59>, < -1.26,  -1.19,  -0.87>, Rbond texture{pigment {color rgb <1.00, 0.05, 0.05> transmit 0.0} finish{ase3}}}
cylinder {< -2.19,  -1.19,  -1.14>, < -2.07,  -0.29,  -1.54>, Rbond texture{pigment {color rgb <0.09, 0.33, 0.53> transmit 0.0} finish{ase3}}}
cylinder {< -1.95,   0.60,  -1.94>, < -2.07,  -0.29,  -1.54>, Rbond texture{pigment {color rgb <1.00, 0.05, 0.05> transmit 0.0} finish{ase3}}}
cylinder {<  1.26,  -0.78,  -1.71>, <  2.05,  -0.42,  -2.20>, Rbond texture{pigment {color rgb <0.40, 0.56, 0.56> transmit 0.0} finish{ase3}}}
cylinder {<  2.83,  -0.06,  -2.69>, <  2.05,  -0.42,  -2.20>, Rbond texture{pigment {color rgb <1.00, 0.05, 0.05> transmit 0.0} finish{ase3}}}
cylinder {<  1.26,  -0.78,  -1.71>, <  1.66,  -1.09,  -0.86>, Rbond texture{pigment {color rgb <0.40, 0.56, 0.56> transmit 0.0} finish{ase3}}}
cylinder {<  2.05,  -1.40,   0.00>, <  1.66,  -1.09,  -0.86>, Rbond texture{pigment {color rgb <1.00, 0.05, 0.05> transmit 0.0} finish{ase3}}}
cylinder {<  1.26,  -0.78,  -1.71>, <  0.86,  -0.32,  -2.49>, Rbond texture{pigment {color rgb <0.40, 0.56, 0.56> transmit 0.0} finish{ase3}}}
cylinder {<  0.45,   0.14,  -3.27>, <  0.86,  -0.32,  -2.49>, Rbond texture{pigment {color rgb <1.00, 0.05, 0.05> transmit 0.0} finish{ase3}}}
cylinder {<  1.26,  -0.78,  -1.71>, <  0.47,  -0.99,  -1.15>, Rbond texture{pigment {color rgb <0.40, 0.56, 0.56> transmit 0.0} finish{ase3}}}
cylinder {< -0.33,  -1.20,  -0.59>, <  0.47,  -0.99,  -1.15>, Rbond texture{pigment {color rgb <1.00, 0.05, 0.05> transmit 0.0} finish{ase3}}}
