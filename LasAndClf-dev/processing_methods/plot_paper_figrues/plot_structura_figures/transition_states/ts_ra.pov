#include "colors.inc"
#include "finish.inc"

global_settings {assumed_gamma 1 max_trace_level 6}
background {color White}
camera {perspective
  right -7.40*x up 5.81*y
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

atom(< -0.98,   0.86,  -1.70>, 0.26, rgb <1.00, 1.00, 1.00>, 0.0, ase3) // #0 
atom(<  1.41,   1.33,  -0.80>, 0.26, rgb <1.00, 1.00, 1.00>, 0.0, ase3) // #1 
atom(<  0.23,   2.50,  -1.64>, 0.26, rgb <1.00, 1.00, 1.00>, 0.0, ase3) // #2 
atom(< -0.22,   1.72,   0.00>, 0.26, rgb <1.00, 1.00, 1.00>, 0.0, ase3) // #3 
atom(<  0.39,   1.72,  -0.90>, 0.65, rgb <0.56, 0.56, 0.56>, 0.0, ase3) // #4 
atom(<  0.56,  -0.17,  -3.50>, 0.56, rgb <1.00, 0.05, 0.05>, 0.0, ase3) // #5 
atom(< -0.19,  -1.47,  -0.91>, 0.56, rgb <1.00, 0.05, 0.05>, 0.0, ase3) // #6 
atom(<  2.23,  -1.51,  -0.26>, 0.56, rgb <1.00, 0.05, 0.05>, 0.0, ase3) // #7 
atom(<  2.96,  -0.24,  -2.81>, 0.56, rgb <1.00, 0.05, 0.05>, 0.0, ase3) // #8 
atom(< -1.07,   1.61,  -4.77>, 0.56, rgb <1.00, 0.05, 0.05>, 0.0, ase3) // #9 
atom(< -1.76,   0.40,  -2.15>, 0.56, rgb <1.00, 0.05, 0.05>, 0.0, ase3) // #10 
atom(<  2.17,   0.13,  -4.57>, 1.36, rgb <0.75, 0.76, 0.78>, 0.0, ase3) // #11 
atom(<  1.40,  -1.13,  -2.01>, 1.36, rgb <0.75, 0.76, 0.78>, 0.0, ase3) // #12 
atom(< -1.40,  -0.08,  -4.06>, 1.36, rgb <0.75, 0.76, 0.78>, 0.0, ase3) // #13 
atom(< -2.17,  -1.41,  -1.40>, 1.36, rgb <0.75, 0.76, 0.78>, 0.0, ase3) // #14 
cylinder {<  0.39,   1.72,  -0.90>, <  0.90,   1.53,  -0.85>, Rbond texture{pigment {color rgb <0.56, 0.56, 0.56> transmit 0.0} finish{ase3}}}
cylinder {<  1.41,   1.33,  -0.80>, <  0.90,   1.53,  -0.85>, Rbond texture{pigment {color rgb <1.00, 1.00, 1.00> transmit 0.0} finish{ase3}}}
cylinder {<  0.39,   1.72,  -0.90>, <  0.31,   2.11,  -1.27>, Rbond texture{pigment {color rgb <0.56, 0.56, 0.56> transmit 0.0} finish{ase3}}}
cylinder {<  0.23,   2.50,  -1.64>, <  0.31,   2.11,  -1.27>, Rbond texture{pigment {color rgb <1.00, 1.00, 1.00> transmit 0.0} finish{ase3}}}
cylinder {<  0.39,   1.72,  -0.90>, <  0.09,   1.72,  -0.45>, Rbond texture{pigment {color rgb <0.56, 0.56, 0.56> transmit 0.0} finish{ase3}}}
cylinder {< -0.22,   1.72,   0.00>, <  0.09,   1.72,  -0.45>, Rbond texture{pigment {color rgb <1.00, 1.00, 1.00> transmit 0.0} finish{ase3}}}
cylinder {< -1.76,   0.40,  -2.15>, < -1.37,   0.63,  -1.93>, Rbond texture{pigment {color rgb <1.00, 0.05, 0.05> transmit 0.0} finish{ase3}}}
cylinder {< -0.98,   0.86,  -1.70>, < -1.37,   0.63,  -1.93>, Rbond texture{pigment {color rgb <1.00, 1.00, 1.00> transmit 0.0} finish{ase3}}}
cylinder {<  2.17,   0.13,  -4.57>, <  1.36,  -0.02,  -4.04>, Rbond texture{pigment {color rgb <0.75, 0.76, 0.78> transmit 0.0} finish{ase3}}}
cylinder {<  0.56,  -0.17,  -3.50>, <  1.36,  -0.02,  -4.04>, Rbond texture{pigment {color rgb <1.00, 0.05, 0.05> transmit 0.0} finish{ase3}}}
cylinder {<  2.17,   0.13,  -4.57>, <  2.56,  -0.05,  -3.69>, Rbond texture{pigment {color rgb <0.75, 0.76, 0.78> transmit 0.0} finish{ase3}}}
cylinder {<  2.96,  -0.24,  -2.81>, <  2.56,  -0.05,  -3.69>, Rbond texture{pigment {color rgb <1.00, 0.05, 0.05> transmit 0.0} finish{ase3}}}
cylinder {<  1.40,  -1.13,  -2.01>, <  0.98,  -0.65,  -2.75>, Rbond texture{pigment {color rgb <0.75, 0.76, 0.78> transmit 0.0} finish{ase3}}}
cylinder {<  0.56,  -0.17,  -3.50>, <  0.98,  -0.65,  -2.75>, Rbond texture{pigment {color rgb <1.00, 0.05, 0.05> transmit 0.0} finish{ase3}}}
cylinder {<  1.40,  -1.13,  -2.01>, <  0.61,  -1.30,  -1.46>, Rbond texture{pigment {color rgb <0.75, 0.76, 0.78> transmit 0.0} finish{ase3}}}
cylinder {< -0.19,  -1.47,  -0.91>, <  0.61,  -1.30,  -1.46>, Rbond texture{pigment {color rgb <1.00, 0.05, 0.05> transmit 0.0} finish{ase3}}}
cylinder {<  1.40,  -1.13,  -2.01>, <  1.82,  -1.32,  -1.13>, Rbond texture{pigment {color rgb <0.75, 0.76, 0.78> transmit 0.0} finish{ase3}}}
cylinder {<  2.23,  -1.51,  -0.26>, <  1.82,  -1.32,  -1.13>, Rbond texture{pigment {color rgb <1.00, 0.05, 0.05> transmit 0.0} finish{ase3}}}
cylinder {<  1.40,  -1.13,  -2.01>, <  2.18,  -0.68,  -2.41>, Rbond texture{pigment {color rgb <0.75, 0.76, 0.78> transmit 0.0} finish{ase3}}}
cylinder {<  2.96,  -0.24,  -2.81>, <  2.18,  -0.68,  -2.41>, Rbond texture{pigment {color rgb <1.00, 0.05, 0.05> transmit 0.0} finish{ase3}}}
cylinder {< -1.40,  -0.08,  -4.06>, < -0.42,  -0.13,  -3.78>, Rbond texture{pigment {color rgb <0.75, 0.76, 0.78> transmit 0.0} finish{ase3}}}
cylinder {<  0.56,  -0.17,  -3.50>, < -0.42,  -0.13,  -3.78>, Rbond texture{pigment {color rgb <1.00, 0.05, 0.05> transmit 0.0} finish{ase3}}}
cylinder {< -1.40,  -0.08,  -4.06>, < -1.23,   0.76,  -4.42>, Rbond texture{pigment {color rgb <0.75, 0.76, 0.78> transmit 0.0} finish{ase3}}}
cylinder {< -1.07,   1.61,  -4.77>, < -1.23,   0.76,  -4.42>, Rbond texture{pigment {color rgb <1.00, 0.05, 0.05> transmit 0.0} finish{ase3}}}
cylinder {< -1.40,  -0.08,  -4.06>, < -1.58,   0.16,  -3.11>, Rbond texture{pigment {color rgb <0.75, 0.76, 0.78> transmit 0.0} finish{ase3}}}
cylinder {< -1.76,   0.40,  -2.15>, < -1.58,   0.16,  -3.11>, Rbond texture{pigment {color rgb <1.00, 0.05, 0.05> transmit 0.0} finish{ase3}}}
cylinder {< -2.17,  -1.41,  -1.40>, < -1.18,  -1.44,  -1.15>, Rbond texture{pigment {color rgb <0.75, 0.76, 0.78> transmit 0.0} finish{ase3}}}
cylinder {< -0.19,  -1.47,  -0.91>, < -1.18,  -1.44,  -1.15>, Rbond texture{pigment {color rgb <1.00, 0.05, 0.05> transmit 0.0} finish{ase3}}}
cylinder {< -2.17,  -1.41,  -1.40>, < -1.96,  -0.50,  -1.78>, Rbond texture{pigment {color rgb <0.75, 0.76, 0.78> transmit 0.0} finish{ase3}}}
cylinder {< -1.76,   0.40,  -2.15>, < -1.96,  -0.50,  -1.78>, Rbond texture{pigment {color rgb <1.00, 0.05, 0.05> transmit 0.0} finish{ase3}}}
