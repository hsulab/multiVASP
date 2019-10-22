#include "colors.inc"
#include "finish.inc"

global_settings {assumed_gamma 1 max_trace_level 6}
background {color White}
camera {perspective
  right -7.45*x up 5.21*y
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

atom(< -0.54,   0.85,  -1.45>, 0.26, rgb <1.00, 1.00, 1.00>, 0.0, ase3) // #0 
atom(<  1.68,   1.22,  -0.37>, 0.26, rgb <1.00, 1.00, 1.00>, 0.0, ase3) // #1 
atom(<  0.91,   2.22,  -1.63>, 0.26, rgb <1.00, 1.00, 1.00>, 0.0, ase3) // #2 
atom(<  0.05,   1.79,  -0.11>, 0.26, rgb <1.00, 1.00, 1.00>, 0.0, ase3) // #3 
atom(<  0.73,   1.42,  -0.90>, 0.65, rgb <0.56, 0.56, 0.56>, 0.0, ase3) // #4 
atom(<  0.56,  -0.03,  -3.36>, 0.56, rgb <1.00, 0.05, 0.05>, 0.0, ase3) // #5 
atom(< -0.22,  -1.34,  -0.63>, 0.56, rgb <1.00, 0.05, 0.05>, 0.0, ase3) // #6 
atom(<  2.94,   0.03,  -2.51>, 0.56, rgb <1.00, 0.05, 0.05>, 0.0, ase3) // #7 
atom(<  2.22,  -1.23,   0.00>, 0.56, rgb <1.00, 0.05, 0.05>, 0.0, ase3) // #8 
atom(< -1.08,   1.86,  -4.50>, 0.56, rgb <1.00, 0.05, 0.05>, 0.0, ase3) // #9 
atom(< -1.58,   0.59,  -1.87>, 0.56, rgb <1.00, 0.05, 0.05>, 0.0, ase3) // #10 
atom(<  2.19,   0.35,  -4.31>, 1.36, rgb <0.75, 0.76, 0.78>, 0.0, ase3) // #11 
atom(<  1.30,  -0.68,  -1.66>, 1.36, rgb <0.75, 0.76, 0.78>, 0.0, ase3) // #12 
atom(< -2.19,  -1.12,  -1.14>, 1.36, rgb <0.75, 0.76, 0.78>, 0.0, ase3) // #13 
atom(< -1.42,   0.19,  -3.78>, 1.36, rgb <0.75, 0.76, 0.78>, 0.0, ase3) // #14 
cylinder {<  0.73,   1.42,  -0.90>, <  1.20,   1.32,  -0.63>, Rbond texture{pigment {color rgb <0.56, 0.56, 0.56> transmit 0.0} finish{ase3}}}
cylinder {<  1.68,   1.22,  -0.37>, <  1.20,   1.32,  -0.63>, Rbond texture{pigment {color rgb <1.00, 1.00, 1.00> transmit 0.0} finish{ase3}}}
cylinder {<  0.73,   1.42,  -0.90>, <  0.82,   1.82,  -1.27>, Rbond texture{pigment {color rgb <0.56, 0.56, 0.56> transmit 0.0} finish{ase3}}}
cylinder {<  0.91,   2.22,  -1.63>, <  0.82,   1.82,  -1.27>, Rbond texture{pigment {color rgb <1.00, 1.00, 1.00> transmit 0.0} finish{ase3}}}
cylinder {<  0.73,   1.42,  -0.90>, <  0.39,   1.61,  -0.51>, Rbond texture{pigment {color rgb <0.56, 0.56, 0.56> transmit 0.0} finish{ase3}}}
cylinder {<  0.05,   1.79,  -0.11>, <  0.39,   1.61,  -0.51>, Rbond texture{pigment {color rgb <1.00, 1.00, 1.00> transmit 0.0} finish{ase3}}}
cylinder {< -1.58,   0.59,  -1.87>, < -1.06,   0.72,  -1.66>, Rbond texture{pigment {color rgb <1.00, 0.05, 0.05> transmit 0.0} finish{ase3}}}
cylinder {< -0.54,   0.85,  -1.45>, < -1.06,   0.72,  -1.66>, Rbond texture{pigment {color rgb <1.00, 1.00, 1.00> transmit 0.0} finish{ase3}}}
cylinder {<  2.19,   0.35,  -4.31>, <  1.37,   0.16,  -3.83>, Rbond texture{pigment {color rgb <0.75, 0.76, 0.78> transmit 0.0} finish{ase3}}}
cylinder {<  0.56,  -0.03,  -3.36>, <  1.37,   0.16,  -3.83>, Rbond texture{pigment {color rgb <1.00, 0.05, 0.05> transmit 0.0} finish{ase3}}}
cylinder {<  2.19,   0.35,  -4.31>, <  2.56,   0.19,  -3.41>, Rbond texture{pigment {color rgb <0.75, 0.76, 0.78> transmit 0.0} finish{ase3}}}
cylinder {<  2.94,   0.03,  -2.51>, <  2.56,   0.19,  -3.41>, Rbond texture{pigment {color rgb <1.00, 0.05, 0.05> transmit 0.0} finish{ase3}}}
cylinder {<  1.30,  -0.68,  -1.66>, <  1.01,   0.37,  -1.28>, Rbond texture{pigment {color rgb <0.75, 0.76, 0.78> transmit 0.0} finish{ase3}}}
cylinder {<  0.73,   1.42,  -0.90>, <  1.01,   0.37,  -1.28>, Rbond texture{pigment {color rgb <0.56, 0.56, 0.56> transmit 0.0} finish{ase3}}}
cylinder {<  1.30,  -0.68,  -1.66>, <  0.93,  -0.35,  -2.51>, Rbond texture{pigment {color rgb <0.75, 0.76, 0.78> transmit 0.0} finish{ase3}}}
cylinder {<  0.56,  -0.03,  -3.36>, <  0.93,  -0.35,  -2.51>, Rbond texture{pigment {color rgb <1.00, 0.05, 0.05> transmit 0.0} finish{ase3}}}
cylinder {<  1.30,  -0.68,  -1.66>, <  0.54,  -1.01,  -1.15>, Rbond texture{pigment {color rgb <0.75, 0.76, 0.78> transmit 0.0} finish{ase3}}}
cylinder {< -0.22,  -1.34,  -0.63>, <  0.54,  -1.01,  -1.15>, Rbond texture{pigment {color rgb <1.00, 0.05, 0.05> transmit 0.0} finish{ase3}}}
cylinder {<  1.30,  -0.68,  -1.66>, <  2.12,  -0.32,  -2.09>, Rbond texture{pigment {color rgb <0.75, 0.76, 0.78> transmit 0.0} finish{ase3}}}
cylinder {<  2.94,   0.03,  -2.51>, <  2.12,  -0.32,  -2.09>, Rbond texture{pigment {color rgb <1.00, 0.05, 0.05> transmit 0.0} finish{ase3}}}
cylinder {<  1.30,  -0.68,  -1.66>, <  1.76,  -0.96,  -0.83>, Rbond texture{pigment {color rgb <0.75, 0.76, 0.78> transmit 0.0} finish{ase3}}}
cylinder {<  2.22,  -1.23,   0.00>, <  1.76,  -0.96,  -0.83>, Rbond texture{pigment {color rgb <1.00, 0.05, 0.05> transmit 0.0} finish{ase3}}}
cylinder {< -2.19,  -1.12,  -1.14>, < -1.20,  -1.23,  -0.88>, Rbond texture{pigment {color rgb <0.75, 0.76, 0.78> transmit 0.0} finish{ase3}}}
cylinder {< -0.22,  -1.34,  -0.63>, < -1.20,  -1.23,  -0.88>, Rbond texture{pigment {color rgb <1.00, 0.05, 0.05> transmit 0.0} finish{ase3}}}
cylinder {< -2.19,  -1.12,  -1.14>, < -1.88,  -0.27,  -1.51>, Rbond texture{pigment {color rgb <0.75, 0.76, 0.78> transmit 0.0} finish{ase3}}}
cylinder {< -1.58,   0.59,  -1.87>, < -1.88,  -0.27,  -1.51>, Rbond texture{pigment {color rgb <1.00, 0.05, 0.05> transmit 0.0} finish{ase3}}}
cylinder {< -1.42,   0.19,  -3.78>, < -0.43,   0.08,  -3.57>, Rbond texture{pigment {color rgb <0.75, 0.76, 0.78> transmit 0.0} finish{ase3}}}
cylinder {<  0.56,  -0.03,  -3.36>, < -0.43,   0.08,  -3.57>, Rbond texture{pigment {color rgb <1.00, 0.05, 0.05> transmit 0.0} finish{ase3}}}
cylinder {< -1.42,   0.19,  -3.78>, < -1.25,   1.03,  -4.14>, Rbond texture{pigment {color rgb <0.75, 0.76, 0.78> transmit 0.0} finish{ase3}}}
cylinder {< -1.08,   1.86,  -4.50>, < -1.25,   1.03,  -4.14>, Rbond texture{pigment {color rgb <1.00, 0.05, 0.05> transmit 0.0} finish{ase3}}}
cylinder {< -1.42,   0.19,  -3.78>, < -1.50,   0.39,  -2.83>, Rbond texture{pigment {color rgb <0.75, 0.76, 0.78> transmit 0.0} finish{ase3}}}
cylinder {< -1.58,   0.59,  -1.87>, < -1.50,   0.39,  -2.83>, Rbond texture{pigment {color rgb <1.00, 0.05, 0.05> transmit 0.0} finish{ase3}}}
