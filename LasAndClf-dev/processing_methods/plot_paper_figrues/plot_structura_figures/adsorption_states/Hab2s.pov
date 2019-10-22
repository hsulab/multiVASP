#include "colors.inc"
#include "finish.inc"

global_settings {assumed_gamma 1 max_trace_level 6}
background {color White}
camera {perspective
  right -7.20*x up 14.49*y
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

atom(< -2.23,   6.63,  -1.55>, 0.26, rgb <1.00, 1.00, 1.00>, 0.0, ase3) // #0 
atom(<  0.93,  -6.34,  -4.48>, 0.56, rgb <1.00, 0.05, 0.05>, 0.0, ase3) // #1 
atom(<  0.93,  -6.34,  -1.55>, 0.56, rgb <1.00, 0.05, 0.05>, 0.0, ase3) // #2 
atom(< -1.00,  -5.11,  -3.01>, 0.56, rgb <1.00, 0.05, 0.05>, 0.0, ase3) // #3 
atom(< -1.00,  -5.11,  -0.09>, 0.56, rgb <1.00, 0.05, 0.05>, 0.0, ase3) // #4 
atom(<  2.87,  -5.11,  -3.01>, 0.56, rgb <1.00, 0.05, 0.05>, 0.0, ase3) // #5 
atom(<  2.87,  -5.11,  -0.09>, 0.56, rgb <1.00, 0.05, 0.05>, 0.0, ase3) // #6 
atom(<  0.93,  -3.89,  -4.48>, 0.56, rgb <1.00, 0.05, 0.05>, 0.0, ase3) // #7 
atom(<  0.93,  -3.89,  -1.55>, 0.56, rgb <1.00, 0.05, 0.05>, 0.0, ase3) // #8 
atom(< -2.23,  -3.18,  -4.48>, 0.56, rgb <1.00, 0.05, 0.05>, 0.0, ase3) // #9 
atom(< -2.23,  -3.18,  -1.55>, 0.56, rgb <1.00, 0.05, 0.05>, 0.0, ase3) // #10 
atom(< -0.29,  -1.95,  -3.01>, 0.56, rgb <1.00, 0.05, 0.05>, 0.0, ase3) // #11 
atom(< -0.29,  -1.95,  -0.09>, 0.56, rgb <1.00, 0.05, 0.05>, 0.0, ase3) // #12 
atom(<  2.16,  -1.95,  -3.01>, 0.56, rgb <1.00, 0.05, 0.05>, 0.0, ase3) // #13 
atom(<  2.16,  -1.95,  -0.09>, 0.56, rgb <1.00, 0.05, 0.05>, 0.0, ase3) // #14 
atom(< -2.23,  -0.73,  -4.48>, 0.56, rgb <1.00, 0.05, 0.05>, 0.0, ase3) // #15 
atom(< -2.23,  -0.73,  -1.55>, 0.56, rgb <1.00, 0.05, 0.05>, 0.0, ase3) // #16 
atom(<  0.93,  -0.03,  -4.48>, 0.56, rgb <1.00, 0.05, 0.05>, 0.0, ase3) // #17 
atom(<  0.93,  -0.02,  -1.55>, 0.56, rgb <1.00, 0.05, 0.05>, 0.0, ase3) // #18 
atom(< -1.00,   1.22,  -3.01>, 0.56, rgb <1.00, 0.05, 0.05>, 0.0, ase3) // #19 
atom(< -1.00,   1.22,  -0.10>, 0.56, rgb <1.00, 0.05, 0.05>, 0.0, ase3) // #20 
atom(<  2.86,   1.22,  -3.01>, 0.56, rgb <1.00, 0.05, 0.05>, 0.0, ase3) // #21 
atom(<  2.86,   1.22,  -0.10>, 0.56, rgb <1.00, 0.05, 0.05>, 0.0, ase3) // #22 
atom(<  0.93,   2.39,  -4.48>, 0.56, rgb <1.00, 0.05, 0.05>, 0.0, ase3) // #23 
atom(<  0.93,   2.42,  -1.55>, 0.56, rgb <1.00, 0.05, 0.05>, 0.0, ase3) // #24 
atom(< -2.23,   3.12,  -4.48>, 0.56, rgb <1.00, 0.05, 0.05>, 0.0, ase3) // #25 
atom(< -2.23,   3.26,  -1.55>, 0.56, rgb <1.00, 0.05, 0.05>, 0.0, ase3) // #26 
atom(< -0.30,   4.54,  -3.11>, 0.56, rgb <1.00, 0.05, 0.05>, 0.0, ase3) // #27 
atom(< -0.30,   4.54,  -0.00>, 0.56, rgb <1.00, 0.05, 0.05>, 0.0, ase3) // #28 
atom(<  2.16,   4.54,  -3.11>, 0.56, rgb <1.00, 0.05, 0.05>, 0.0, ase3) // #29 
atom(<  2.16,   4.54,   0.00>, 0.56, rgb <1.00, 0.05, 0.05>, 0.0, ase3) // #30 
atom(< -2.23,   5.68,  -4.48>, 0.56, rgb <1.00, 0.05, 0.05>, 0.0, ase3) // #31 
atom(< -2.23,   5.66,  -1.55>, 0.56, rgb <1.00, 0.05, 0.05>, 0.0, ase3) // #32 
atom(< -2.23,  -5.11,  -4.48>, 1.20, rgb <0.09, 0.33, 0.53>, 0.0, ase3) // #33 
atom(< -2.23,  -5.11,  -1.55>, 1.20, rgb <0.09, 0.33, 0.53>, 0.0, ase3) // #34 
atom(<  0.93,  -5.11,  -3.01>, 1.20, rgb <0.09, 0.33, 0.53>, 0.0, ase3) // #35 
atom(<  0.93,  -5.11,  -0.09>, 1.20, rgb <0.09, 0.33, 0.53>, 0.0, ase3) // #36 
atom(< -2.23,  -1.95,  -3.01>, 1.20, rgb <0.09, 0.33, 0.53>, 0.0, ase3) // #37 
atom(< -2.23,  -1.95,  -0.09>, 1.20, rgb <0.09, 0.33, 0.53>, 0.0, ase3) // #38 
atom(<  0.93,  -1.95,  -4.48>, 1.20, rgb <0.09, 0.33, 0.53>, 0.0, ase3) // #39 
atom(<  0.93,  -1.95,  -1.55>, 1.20, rgb <0.09, 0.33, 0.53>, 0.0, ase3) // #40 
atom(< -2.23,   1.22,  -4.48>, 1.20, rgb <0.09, 0.33, 0.53>, 0.0, ase3) // #41 
atom(< -2.23,   1.26,  -1.55>, 1.20, rgb <0.09, 0.33, 0.53>, 0.0, ase3) // #42 
atom(<  0.93,   1.17,  -3.01>, 1.20, rgb <0.09, 0.33, 0.53>, 0.0, ase3) // #43 
atom(<  0.93,   1.17,  -0.09>, 1.20, rgb <0.09, 0.33, 0.53>, 0.0, ase3) // #44 
atom(< -2.23,   4.46,  -3.09>, 1.20, rgb <0.09, 0.33, 0.53>, 0.0, ase3) // #45 
atom(< -2.23,   4.46,  -0.01>, 1.20, rgb <0.09, 0.33, 0.53>, 0.0, ase3) // #46 
atom(<  0.93,   4.24,  -4.48>, 1.20, rgb <0.09, 0.33, 0.53>, 0.0, ase3) // #47 
atom(<  0.93,   4.38,  -1.55>, 1.02, rgb <0.40, 0.56, 0.56>, 0.0, ase3) // #48 
cylinder {< -2.23,   5.66,  -1.55>, < -2.23,   6.15,  -1.55>, Rbond texture{pigment {color rgb <1.00, 0.05, 0.05> transmit 0.0} finish{ase3}}}
cylinder {< -2.23,   6.63,  -1.55>, < -2.23,   6.15,  -1.55>, Rbond texture{pigment {color rgb <1.00, 1.00, 1.00> transmit 0.0} finish{ase3}}}
cylinder {< -2.23,  -5.11,  -4.48>, < -1.62,  -5.11,  -3.75>, Rbond texture{pigment {color rgb <0.09, 0.33, 0.53> transmit 0.0} finish{ase3}}}
cylinder {< -1.00,  -5.11,  -3.01>, < -1.62,  -5.11,  -3.75>, Rbond texture{pigment {color rgb <1.00, 0.05, 0.05> transmit 0.0} finish{ase3}}}
cylinder {< -2.23,  -5.11,  -4.48>, < -2.23,  -4.14,  -4.48>, Rbond texture{pigment {color rgb <0.09, 0.33, 0.53> transmit 0.0} finish{ase3}}}
cylinder {< -2.23,  -3.18,  -4.48>, < -2.23,  -4.14,  -4.48>, Rbond texture{pigment {color rgb <1.00, 0.05, 0.05> transmit 0.0} finish{ase3}}}
cylinder {< -2.23,  -5.11,  -1.55>, < -1.62,  -5.11,  -2.28>, Rbond texture{pigment {color rgb <0.09, 0.33, 0.53> transmit 0.0} finish{ase3}}}
cylinder {< -1.00,  -5.11,  -3.01>, < -1.62,  -5.11,  -2.28>, Rbond texture{pigment {color rgb <1.00, 0.05, 0.05> transmit 0.0} finish{ase3}}}
cylinder {< -2.23,  -5.11,  -1.55>, < -1.62,  -5.11,  -0.82>, Rbond texture{pigment {color rgb <0.09, 0.33, 0.53> transmit 0.0} finish{ase3}}}
cylinder {< -1.00,  -5.11,  -0.09>, < -1.62,  -5.11,  -0.82>, Rbond texture{pigment {color rgb <1.00, 0.05, 0.05> transmit 0.0} finish{ase3}}}
cylinder {< -2.23,  -5.11,  -1.55>, < -2.23,  -4.14,  -1.55>, Rbond texture{pigment {color rgb <0.09, 0.33, 0.53> transmit 0.0} finish{ase3}}}
cylinder {< -2.23,  -3.18,  -1.55>, < -2.23,  -4.14,  -1.55>, Rbond texture{pigment {color rgb <1.00, 0.05, 0.05> transmit 0.0} finish{ase3}}}
cylinder {<  0.93,  -5.11,  -3.01>, <  0.93,  -5.72,  -3.75>, Rbond texture{pigment {color rgb <0.09, 0.33, 0.53> transmit 0.0} finish{ase3}}}
cylinder {<  0.93,  -6.34,  -4.48>, <  0.93,  -5.72,  -3.75>, Rbond texture{pigment {color rgb <1.00, 0.05, 0.05> transmit 0.0} finish{ase3}}}
cylinder {<  0.93,  -5.11,  -3.01>, <  0.93,  -5.72,  -2.28>, Rbond texture{pigment {color rgb <0.09, 0.33, 0.53> transmit 0.0} finish{ase3}}}
cylinder {<  0.93,  -6.34,  -1.55>, <  0.93,  -5.72,  -2.28>, Rbond texture{pigment {color rgb <1.00, 0.05, 0.05> transmit 0.0} finish{ase3}}}
cylinder {<  0.93,  -5.11,  -3.01>, < -0.04,  -5.11,  -3.01>, Rbond texture{pigment {color rgb <0.09, 0.33, 0.53> transmit 0.0} finish{ase3}}}
cylinder {< -1.00,  -5.11,  -3.01>, < -0.04,  -5.11,  -3.01>, Rbond texture{pigment {color rgb <1.00, 0.05, 0.05> transmit 0.0} finish{ase3}}}
cylinder {<  0.93,  -5.11,  -3.01>, <  1.90,  -5.11,  -3.01>, Rbond texture{pigment {color rgb <0.09, 0.33, 0.53> transmit 0.0} finish{ase3}}}
cylinder {<  2.87,  -5.11,  -3.01>, <  1.90,  -5.11,  -3.01>, Rbond texture{pigment {color rgb <1.00, 0.05, 0.05> transmit 0.0} finish{ase3}}}
cylinder {<  0.93,  -5.11,  -3.01>, <  0.93,  -4.50,  -3.75>, Rbond texture{pigment {color rgb <0.09, 0.33, 0.53> transmit 0.0} finish{ase3}}}
cylinder {<  0.93,  -3.89,  -4.48>, <  0.93,  -4.50,  -3.75>, Rbond texture{pigment {color rgb <1.00, 0.05, 0.05> transmit 0.0} finish{ase3}}}
cylinder {<  0.93,  -5.11,  -3.01>, <  0.93,  -4.50,  -2.28>, Rbond texture{pigment {color rgb <0.09, 0.33, 0.53> transmit 0.0} finish{ase3}}}
cylinder {<  0.93,  -3.89,  -1.55>, <  0.93,  -4.50,  -2.28>, Rbond texture{pigment {color rgb <1.00, 0.05, 0.05> transmit 0.0} finish{ase3}}}
cylinder {<  0.93,  -5.11,  -0.09>, <  0.93,  -5.72,  -0.82>, Rbond texture{pigment {color rgb <0.09, 0.33, 0.53> transmit 0.0} finish{ase3}}}
cylinder {<  0.93,  -6.34,  -1.55>, <  0.93,  -5.72,  -0.82>, Rbond texture{pigment {color rgb <1.00, 0.05, 0.05> transmit 0.0} finish{ase3}}}
cylinder {<  0.93,  -5.11,  -0.09>, < -0.04,  -5.11,  -0.09>, Rbond texture{pigment {color rgb <0.09, 0.33, 0.53> transmit 0.0} finish{ase3}}}
cylinder {< -1.00,  -5.11,  -0.09>, < -0.04,  -5.11,  -0.09>, Rbond texture{pigment {color rgb <1.00, 0.05, 0.05> transmit 0.0} finish{ase3}}}
cylinder {<  0.93,  -5.11,  -0.09>, <  1.90,  -5.11,  -0.09>, Rbond texture{pigment {color rgb <0.09, 0.33, 0.53> transmit 0.0} finish{ase3}}}
cylinder {<  2.87,  -5.11,  -0.09>, <  1.90,  -5.11,  -0.09>, Rbond texture{pigment {color rgb <1.00, 0.05, 0.05> transmit 0.0} finish{ase3}}}
cylinder {<  0.93,  -5.11,  -0.09>, <  0.93,  -4.50,  -0.82>, Rbond texture{pigment {color rgb <0.09, 0.33, 0.53> transmit 0.0} finish{ase3}}}
cylinder {<  0.93,  -3.89,  -1.55>, <  0.93,  -4.50,  -0.82>, Rbond texture{pigment {color rgb <1.00, 0.05, 0.05> transmit 0.0} finish{ase3}}}
cylinder {< -2.23,  -1.95,  -3.01>, < -2.23,  -2.56,  -3.75>, Rbond texture{pigment {color rgb <0.09, 0.33, 0.53> transmit 0.0} finish{ase3}}}
cylinder {< -2.23,  -3.18,  -4.48>, < -2.23,  -2.56,  -3.75>, Rbond texture{pigment {color rgb <1.00, 0.05, 0.05> transmit 0.0} finish{ase3}}}
cylinder {< -2.23,  -1.95,  -3.01>, < -2.23,  -2.56,  -2.28>, Rbond texture{pigment {color rgb <0.09, 0.33, 0.53> transmit 0.0} finish{ase3}}}
cylinder {< -2.23,  -3.18,  -1.55>, < -2.23,  -2.56,  -2.28>, Rbond texture{pigment {color rgb <1.00, 0.05, 0.05> transmit 0.0} finish{ase3}}}
cylinder {< -2.23,  -1.95,  -3.01>, < -1.26,  -1.95,  -3.01>, Rbond texture{pigment {color rgb <0.09, 0.33, 0.53> transmit 0.0} finish{ase3}}}
cylinder {< -0.29,  -1.95,  -3.01>, < -1.26,  -1.95,  -3.01>, Rbond texture{pigment {color rgb <1.00, 0.05, 0.05> transmit 0.0} finish{ase3}}}
cylinder {< -2.23,  -1.95,  -3.01>, < -2.23,  -1.34,  -3.75>, Rbond texture{pigment {color rgb <0.09, 0.33, 0.53> transmit 0.0} finish{ase3}}}
cylinder {< -2.23,  -0.73,  -4.48>, < -2.23,  -1.34,  -3.75>, Rbond texture{pigment {color rgb <1.00, 0.05, 0.05> transmit 0.0} finish{ase3}}}
cylinder {< -2.23,  -1.95,  -3.01>, < -2.23,  -1.34,  -2.28>, Rbond texture{pigment {color rgb <0.09, 0.33, 0.53> transmit 0.0} finish{ase3}}}
cylinder {< -2.23,  -0.73,  -1.55>, < -2.23,  -1.34,  -2.28>, Rbond texture{pigment {color rgb <1.00, 0.05, 0.05> transmit 0.0} finish{ase3}}}
cylinder {< -2.23,  -1.95,  -0.09>, < -2.23,  -2.56,  -0.82>, Rbond texture{pigment {color rgb <0.09, 0.33, 0.53> transmit 0.0} finish{ase3}}}
cylinder {< -2.23,  -3.18,  -1.55>, < -2.23,  -2.56,  -0.82>, Rbond texture{pigment {color rgb <1.00, 0.05, 0.05> transmit 0.0} finish{ase3}}}
cylinder {< -2.23,  -1.95,  -0.09>, < -1.26,  -1.95,  -0.09>, Rbond texture{pigment {color rgb <0.09, 0.33, 0.53> transmit 0.0} finish{ase3}}}
cylinder {< -0.29,  -1.95,  -0.09>, < -1.26,  -1.95,  -0.09>, Rbond texture{pigment {color rgb <1.00, 0.05, 0.05> transmit 0.0} finish{ase3}}}
cylinder {< -2.23,  -1.95,  -0.09>, < -2.23,  -1.34,  -0.82>, Rbond texture{pigment {color rgb <0.09, 0.33, 0.53> transmit 0.0} finish{ase3}}}
cylinder {< -2.23,  -0.73,  -1.55>, < -2.23,  -1.34,  -0.82>, Rbond texture{pigment {color rgb <1.00, 0.05, 0.05> transmit 0.0} finish{ase3}}}
cylinder {<  0.93,  -1.95,  -4.48>, <  0.93,  -2.92,  -4.48>, Rbond texture{pigment {color rgb <0.09, 0.33, 0.53> transmit 0.0} finish{ase3}}}
cylinder {<  0.93,  -3.89,  -4.48>, <  0.93,  -2.92,  -4.48>, Rbond texture{pigment {color rgb <1.00, 0.05, 0.05> transmit 0.0} finish{ase3}}}
cylinder {<  0.93,  -1.95,  -4.48>, <  0.32,  -1.95,  -3.75>, Rbond texture{pigment {color rgb <0.09, 0.33, 0.53> transmit 0.0} finish{ase3}}}
cylinder {< -0.29,  -1.95,  -3.01>, <  0.32,  -1.95,  -3.75>, Rbond texture{pigment {color rgb <1.00, 0.05, 0.05> transmit 0.0} finish{ase3}}}
cylinder {<  0.93,  -1.95,  -4.48>, <  1.54,  -1.95,  -3.75>, Rbond texture{pigment {color rgb <0.09, 0.33, 0.53> transmit 0.0} finish{ase3}}}
cylinder {<  2.16,  -1.95,  -3.01>, <  1.54,  -1.95,  -3.75>, Rbond texture{pigment {color rgb <1.00, 0.05, 0.05> transmit 0.0} finish{ase3}}}
cylinder {<  0.93,  -1.95,  -4.48>, <  0.93,  -0.99,  -4.48>, Rbond texture{pigment {color rgb <0.09, 0.33, 0.53> transmit 0.0} finish{ase3}}}
cylinder {<  0.93,  -0.03,  -4.48>, <  0.93,  -0.99,  -4.48>, Rbond texture{pigment {color rgb <1.00, 0.05, 0.05> transmit 0.0} finish{ase3}}}
cylinder {<  0.93,  -1.95,  -1.55>, <  0.93,  -2.92,  -1.55>, Rbond texture{pigment {color rgb <0.09, 0.33, 0.53> transmit 0.0} finish{ase3}}}
cylinder {<  0.93,  -3.89,  -1.55>, <  0.93,  -2.92,  -1.55>, Rbond texture{pigment {color rgb <1.00, 0.05, 0.05> transmit 0.0} finish{ase3}}}
cylinder {<  0.93,  -1.95,  -1.55>, <  0.32,  -1.95,  -2.28>, Rbond texture{pigment {color rgb <0.09, 0.33, 0.53> transmit 0.0} finish{ase3}}}
cylinder {< -0.29,  -1.95,  -3.01>, <  0.32,  -1.95,  -2.28>, Rbond texture{pigment {color rgb <1.00, 0.05, 0.05> transmit 0.0} finish{ase3}}}
cylinder {<  0.93,  -1.95,  -1.55>, <  0.32,  -1.95,  -0.82>, Rbond texture{pigment {color rgb <0.09, 0.33, 0.53> transmit 0.0} finish{ase3}}}
cylinder {< -0.29,  -1.95,  -0.09>, <  0.32,  -1.95,  -0.82>, Rbond texture{pigment {color rgb <1.00, 0.05, 0.05> transmit 0.0} finish{ase3}}}
cylinder {<  0.93,  -1.95,  -1.55>, <  1.54,  -1.95,  -2.28>, Rbond texture{pigment {color rgb <0.09, 0.33, 0.53> transmit 0.0} finish{ase3}}}
cylinder {<  2.16,  -1.95,  -3.01>, <  1.54,  -1.95,  -2.28>, Rbond texture{pigment {color rgb <1.00, 0.05, 0.05> transmit 0.0} finish{ase3}}}
cylinder {<  0.93,  -1.95,  -1.55>, <  1.54,  -1.95,  -0.82>, Rbond texture{pigment {color rgb <0.09, 0.33, 0.53> transmit 0.0} finish{ase3}}}
cylinder {<  2.16,  -1.95,  -0.09>, <  1.54,  -1.95,  -0.82>, Rbond texture{pigment {color rgb <1.00, 0.05, 0.05> transmit 0.0} finish{ase3}}}
cylinder {<  0.93,  -1.95,  -1.55>, <  0.93,  -0.99,  -1.55>, Rbond texture{pigment {color rgb <0.09, 0.33, 0.53> transmit 0.0} finish{ase3}}}
cylinder {<  0.93,  -0.02,  -1.55>, <  0.93,  -0.99,  -1.55>, Rbond texture{pigment {color rgb <1.00, 0.05, 0.05> transmit 0.0} finish{ase3}}}
cylinder {< -2.23,   1.22,  -4.48>, < -2.23,   0.24,  -4.48>, Rbond texture{pigment {color rgb <0.09, 0.33, 0.53> transmit 0.0} finish{ase3}}}
cylinder {< -2.23,  -0.73,  -4.48>, < -2.23,   0.24,  -4.48>, Rbond texture{pigment {color rgb <1.00, 0.05, 0.05> transmit 0.0} finish{ase3}}}
cylinder {< -2.23,   1.22,  -4.48>, < -1.61,   1.22,  -3.74>, Rbond texture{pigment {color rgb <0.09, 0.33, 0.53> transmit 0.0} finish{ase3}}}
cylinder {< -1.00,   1.22,  -3.01>, < -1.61,   1.22,  -3.74>, Rbond texture{pigment {color rgb <1.00, 0.05, 0.05> transmit 0.0} finish{ase3}}}
cylinder {< -2.23,   1.22,  -4.48>, < -2.23,   2.17,  -4.48>, Rbond texture{pigment {color rgb <0.09, 0.33, 0.53> transmit 0.0} finish{ase3}}}
cylinder {< -2.23,   3.12,  -4.48>, < -2.23,   2.17,  -4.48>, Rbond texture{pigment {color rgb <1.00, 0.05, 0.05> transmit 0.0} finish{ase3}}}
cylinder {< -2.23,   1.26,  -1.55>, < -2.23,   0.27,  -1.55>, Rbond texture{pigment {color rgb <0.09, 0.33, 0.53> transmit 0.0} finish{ase3}}}
cylinder {< -2.23,  -0.73,  -1.55>, < -2.23,   0.27,  -1.55>, Rbond texture{pigment {color rgb <1.00, 0.05, 0.05> transmit 0.0} finish{ase3}}}
cylinder {< -2.23,   1.26,  -1.55>, < -1.61,   1.24,  -2.28>, Rbond texture{pigment {color rgb <0.09, 0.33, 0.53> transmit 0.0} finish{ase3}}}
cylinder {< -1.00,   1.22,  -3.01>, < -1.61,   1.24,  -2.28>, Rbond texture{pigment {color rgb <1.00, 0.05, 0.05> transmit 0.0} finish{ase3}}}
cylinder {< -2.23,   1.26,  -1.55>, < -1.61,   1.24,  -0.83>, Rbond texture{pigment {color rgb <0.09, 0.33, 0.53> transmit 0.0} finish{ase3}}}
cylinder {< -1.00,   1.22,  -0.10>, < -1.61,   1.24,  -0.83>, Rbond texture{pigment {color rgb <1.00, 0.05, 0.05> transmit 0.0} finish{ase3}}}
cylinder {< -2.23,   1.26,  -1.55>, < -2.23,   2.26,  -1.55>, Rbond texture{pigment {color rgb <0.09, 0.33, 0.53> transmit 0.0} finish{ase3}}}
cylinder {< -2.23,   3.26,  -1.55>, < -2.23,   2.26,  -1.55>, Rbond texture{pigment {color rgb <1.00, 0.05, 0.05> transmit 0.0} finish{ase3}}}
cylinder {<  0.93,   1.17,  -3.01>, <  0.93,   0.57,  -3.74>, Rbond texture{pigment {color rgb <0.09, 0.33, 0.53> transmit 0.0} finish{ase3}}}
cylinder {<  0.93,  -0.03,  -4.48>, <  0.93,   0.57,  -3.74>, Rbond texture{pigment {color rgb <1.00, 0.05, 0.05> transmit 0.0} finish{ase3}}}
cylinder {<  0.93,   1.17,  -3.01>, <  0.93,   0.58,  -2.28>, Rbond texture{pigment {color rgb <0.09, 0.33, 0.53> transmit 0.0} finish{ase3}}}
cylinder {<  0.93,  -0.02,  -1.55>, <  0.93,   0.58,  -2.28>, Rbond texture{pigment {color rgb <1.00, 0.05, 0.05> transmit 0.0} finish{ase3}}}
cylinder {<  0.93,   1.17,  -3.01>, < -0.03,   1.20,  -3.01>, Rbond texture{pigment {color rgb <0.09, 0.33, 0.53> transmit 0.0} finish{ase3}}}
cylinder {< -1.00,   1.22,  -3.01>, < -0.03,   1.20,  -3.01>, Rbond texture{pigment {color rgb <1.00, 0.05, 0.05> transmit 0.0} finish{ase3}}}
cylinder {<  0.93,   1.17,  -3.01>, <  1.90,   1.20,  -3.01>, Rbond texture{pigment {color rgb <0.09, 0.33, 0.53> transmit 0.0} finish{ase3}}}
cylinder {<  2.86,   1.22,  -3.01>, <  1.90,   1.20,  -3.01>, Rbond texture{pigment {color rgb <1.00, 0.05, 0.05> transmit 0.0} finish{ase3}}}
cylinder {<  0.93,   1.17,  -3.01>, <  0.93,   1.78,  -3.74>, Rbond texture{pigment {color rgb <0.09, 0.33, 0.53> transmit 0.0} finish{ase3}}}
cylinder {<  0.93,   2.39,  -4.48>, <  0.93,   1.78,  -3.74>, Rbond texture{pigment {color rgb <1.00, 0.05, 0.05> transmit 0.0} finish{ase3}}}
cylinder {<  0.93,   1.17,  -3.01>, <  0.93,   1.80,  -2.28>, Rbond texture{pigment {color rgb <0.09, 0.33, 0.53> transmit 0.0} finish{ase3}}}
cylinder {<  0.93,   2.42,  -1.55>, <  0.93,   1.80,  -2.28>, Rbond texture{pigment {color rgb <1.00, 0.05, 0.05> transmit 0.0} finish{ase3}}}
cylinder {<  0.93,   1.17,  -0.09>, <  0.93,   0.58,  -0.82>, Rbond texture{pigment {color rgb <0.09, 0.33, 0.53> transmit 0.0} finish{ase3}}}
cylinder {<  0.93,  -0.02,  -1.55>, <  0.93,   0.58,  -0.82>, Rbond texture{pigment {color rgb <1.00, 0.05, 0.05> transmit 0.0} finish{ase3}}}
cylinder {<  0.93,   1.17,  -0.09>, < -0.03,   1.20,  -0.10>, Rbond texture{pigment {color rgb <0.09, 0.33, 0.53> transmit 0.0} finish{ase3}}}
cylinder {< -1.00,   1.22,  -0.10>, < -0.03,   1.20,  -0.10>, Rbond texture{pigment {color rgb <1.00, 0.05, 0.05> transmit 0.0} finish{ase3}}}
cylinder {<  0.93,   1.17,  -0.09>, <  1.90,   1.20,  -0.10>, Rbond texture{pigment {color rgb <0.09, 0.33, 0.53> transmit 0.0} finish{ase3}}}
cylinder {<  2.86,   1.22,  -0.10>, <  1.90,   1.20,  -0.10>, Rbond texture{pigment {color rgb <1.00, 0.05, 0.05> transmit 0.0} finish{ase3}}}
cylinder {<  0.93,   1.17,  -0.09>, <  0.93,   1.80,  -0.82>, Rbond texture{pigment {color rgb <0.09, 0.33, 0.53> transmit 0.0} finish{ase3}}}
cylinder {<  0.93,   2.42,  -1.55>, <  0.93,   1.80,  -0.82>, Rbond texture{pigment {color rgb <1.00, 0.05, 0.05> transmit 0.0} finish{ase3}}}
cylinder {< -2.23,   4.46,  -3.09>, < -2.23,   3.79,  -3.78>, Rbond texture{pigment {color rgb <0.09, 0.33, 0.53> transmit 0.0} finish{ase3}}}
cylinder {< -2.23,   3.12,  -4.48>, < -2.23,   3.79,  -3.78>, Rbond texture{pigment {color rgb <1.00, 0.05, 0.05> transmit 0.0} finish{ase3}}}
cylinder {< -2.23,   4.46,  -3.09>, < -2.23,   3.86,  -2.32>, Rbond texture{pigment {color rgb <0.09, 0.33, 0.53> transmit 0.0} finish{ase3}}}
cylinder {< -2.23,   3.26,  -1.55>, < -2.23,   3.86,  -2.32>, Rbond texture{pigment {color rgb <1.00, 0.05, 0.05> transmit 0.0} finish{ase3}}}
cylinder {< -2.23,   4.46,  -3.09>, < -1.26,   4.50,  -3.10>, Rbond texture{pigment {color rgb <0.09, 0.33, 0.53> transmit 0.0} finish{ase3}}}
cylinder {< -0.30,   4.54,  -3.11>, < -1.26,   4.50,  -3.10>, Rbond texture{pigment {color rgb <1.00, 0.05, 0.05> transmit 0.0} finish{ase3}}}
cylinder {< -2.23,   4.46,  -3.09>, < -2.23,   5.07,  -3.78>, Rbond texture{pigment {color rgb <0.09, 0.33, 0.53> transmit 0.0} finish{ase3}}}
cylinder {< -2.23,   5.68,  -4.48>, < -2.23,   5.07,  -3.78>, Rbond texture{pigment {color rgb <1.00, 0.05, 0.05> transmit 0.0} finish{ase3}}}
cylinder {< -2.23,   4.46,  -3.09>, < -2.23,   5.06,  -2.32>, Rbond texture{pigment {color rgb <0.09, 0.33, 0.53> transmit 0.0} finish{ase3}}}
cylinder {< -2.23,   5.66,  -1.55>, < -2.23,   5.06,  -2.32>, Rbond texture{pigment {color rgb <1.00, 0.05, 0.05> transmit 0.0} finish{ase3}}}
cylinder {< -2.23,   4.46,  -0.01>, < -2.23,   3.86,  -0.78>, Rbond texture{pigment {color rgb <0.09, 0.33, 0.53> transmit 0.0} finish{ase3}}}
cylinder {< -2.23,   3.26,  -1.55>, < -2.23,   3.86,  -0.78>, Rbond texture{pigment {color rgb <1.00, 0.05, 0.05> transmit 0.0} finish{ase3}}}
cylinder {< -2.23,   4.46,  -0.01>, < -1.26,   4.50,  -0.01>, Rbond texture{pigment {color rgb <0.09, 0.33, 0.53> transmit 0.0} finish{ase3}}}
cylinder {< -0.30,   4.54,  -0.00>, < -1.26,   4.50,  -0.01>, Rbond texture{pigment {color rgb <1.00, 0.05, 0.05> transmit 0.0} finish{ase3}}}
cylinder {< -2.23,   4.46,  -0.01>, < -2.23,   5.06,  -0.78>, Rbond texture{pigment {color rgb <0.09, 0.33, 0.53> transmit 0.0} finish{ase3}}}
cylinder {< -2.23,   5.66,  -1.55>, < -2.23,   5.06,  -0.78>, Rbond texture{pigment {color rgb <1.00, 0.05, 0.05> transmit 0.0} finish{ase3}}}
cylinder {<  0.93,   4.24,  -4.48>, <  0.93,   3.32,  -4.48>, Rbond texture{pigment {color rgb <0.09, 0.33, 0.53> transmit 0.0} finish{ase3}}}
cylinder {<  0.93,   2.39,  -4.48>, <  0.93,   3.32,  -4.48>, Rbond texture{pigment {color rgb <1.00, 0.05, 0.05> transmit 0.0} finish{ase3}}}
cylinder {<  0.93,   4.24,  -4.48>, <  0.32,   4.39,  -3.79>, Rbond texture{pigment {color rgb <0.09, 0.33, 0.53> transmit 0.0} finish{ase3}}}
cylinder {< -0.30,   4.54,  -3.11>, <  0.32,   4.39,  -3.79>, Rbond texture{pigment {color rgb <1.00, 0.05, 0.05> transmit 0.0} finish{ase3}}}
cylinder {<  0.93,   4.24,  -4.48>, <  1.55,   4.39,  -3.79>, Rbond texture{pigment {color rgb <0.09, 0.33, 0.53> transmit 0.0} finish{ase3}}}
cylinder {<  2.16,   4.54,  -3.11>, <  1.55,   4.39,  -3.79>, Rbond texture{pigment {color rgb <1.00, 0.05, 0.05> transmit 0.0} finish{ase3}}}
cylinder {<  0.93,   4.38,  -1.55>, <  0.93,   3.40,  -1.55>, Rbond texture{pigment {color rgb <0.40, 0.56, 0.56> transmit 0.0} finish{ase3}}}
cylinder {<  0.93,   2.42,  -1.55>, <  0.93,   3.40,  -1.55>, Rbond texture{pigment {color rgb <1.00, 0.05, 0.05> transmit 0.0} finish{ase3}}}
cylinder {<  0.93,   4.38,  -1.55>, <  0.32,   4.46,  -2.33>, Rbond texture{pigment {color rgb <0.40, 0.56, 0.56> transmit 0.0} finish{ase3}}}
cylinder {< -0.30,   4.54,  -3.11>, <  0.32,   4.46,  -2.33>, Rbond texture{pigment {color rgb <1.00, 0.05, 0.05> transmit 0.0} finish{ase3}}}
cylinder {<  0.93,   4.38,  -1.55>, <  0.32,   4.46,  -0.78>, Rbond texture{pigment {color rgb <0.40, 0.56, 0.56> transmit 0.0} finish{ase3}}}
cylinder {< -0.30,   4.54,  -0.00>, <  0.32,   4.46,  -0.78>, Rbond texture{pigment {color rgb <1.00, 0.05, 0.05> transmit 0.0} finish{ase3}}}
cylinder {<  0.93,   4.38,  -1.55>, <  1.55,   4.46,  -2.33>, Rbond texture{pigment {color rgb <0.40, 0.56, 0.56> transmit 0.0} finish{ase3}}}
cylinder {<  2.16,   4.54,  -3.11>, <  1.55,   4.46,  -2.33>, Rbond texture{pigment {color rgb <1.00, 0.05, 0.05> transmit 0.0} finish{ase3}}}
cylinder {<  0.93,   4.38,  -1.55>, <  1.55,   4.46,  -0.78>, Rbond texture{pigment {color rgb <0.40, 0.56, 0.56> transmit 0.0} finish{ase3}}}
cylinder {<  2.16,   4.54,   0.00>, <  1.55,   4.46,  -0.78>, Rbond texture{pigment {color rgb <1.00, 0.05, 0.05> transmit 0.0} finish{ase3}}}
