#include "colors.inc"
#include "finish.inc"

global_settings {assumed_gamma 1 max_trace_level 6}
background {color White}
camera {perspective
  right -7.20*x up 14.23*y
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

atom(< -1.57,   6.51,  -1.55>, 0.26, rgb <1.00, 1.00, 1.00>, 0.0, ase3) // #0 
atom(<  0.93,  -6.22,  -4.48>, 0.56, rgb <1.00, 0.05, 0.05>, 0.0, ase3) // #1 
atom(<  0.93,  -6.22,  -1.55>, 0.56, rgb <1.00, 0.05, 0.05>, 0.0, ase3) // #2 
atom(< -1.00,  -4.99,  -3.01>, 0.56, rgb <1.00, 0.05, 0.05>, 0.0, ase3) // #3 
atom(< -1.00,  -4.99,  -0.09>, 0.56, rgb <1.00, 0.05, 0.05>, 0.0, ase3) // #4 
atom(<  2.87,  -4.99,  -3.01>, 0.56, rgb <1.00, 0.05, 0.05>, 0.0, ase3) // #5 
atom(<  2.87,  -4.99,  -0.09>, 0.56, rgb <1.00, 0.05, 0.05>, 0.0, ase3) // #6 
atom(<  0.93,  -3.76,  -4.48>, 0.56, rgb <1.00, 0.05, 0.05>, 0.0, ase3) // #7 
atom(<  0.93,  -3.76,  -1.55>, 0.56, rgb <1.00, 0.05, 0.05>, 0.0, ase3) // #8 
atom(< -2.23,  -3.06,  -4.48>, 0.56, rgb <1.00, 0.05, 0.05>, 0.0, ase3) // #9 
atom(< -2.23,  -3.06,  -1.55>, 0.56, rgb <1.00, 0.05, 0.05>, 0.0, ase3) // #10 
atom(< -0.29,  -1.83,  -3.01>, 0.56, rgb <1.00, 0.05, 0.05>, 0.0, ase3) // #11 
atom(< -0.29,  -1.83,  -0.09>, 0.56, rgb <1.00, 0.05, 0.05>, 0.0, ase3) // #12 
atom(<  2.16,  -1.83,  -3.01>, 0.56, rgb <1.00, 0.05, 0.05>, 0.0, ase3) // #13 
atom(<  2.16,  -1.83,  -0.09>, 0.56, rgb <1.00, 0.05, 0.05>, 0.0, ase3) // #14 
atom(< -2.23,  -0.61,  -4.48>, 0.56, rgb <1.00, 0.05, 0.05>, 0.0, ase3) // #15 
atom(< -2.23,  -0.61,  -1.55>, 0.56, rgb <1.00, 0.05, 0.05>, 0.0, ase3) // #16 
atom(<  0.93,   0.10,  -4.48>, 0.56, rgb <1.00, 0.05, 0.05>, 0.0, ase3) // #17 
atom(<  0.93,   0.11,  -1.55>, 0.56, rgb <1.00, 0.05, 0.05>, 0.0, ase3) // #18 
atom(< -1.00,   1.33,  -3.01>, 0.56, rgb <1.00, 0.05, 0.05>, 0.0, ase3) // #19 
atom(< -1.00,   1.33,  -0.10>, 0.56, rgb <1.00, 0.05, 0.05>, 0.0, ase3) // #20 
atom(<  2.86,   1.36,  -3.01>, 0.56, rgb <1.00, 0.05, 0.05>, 0.0, ase3) // #21 
atom(<  2.86,   1.36,  -0.10>, 0.56, rgb <1.00, 0.05, 0.05>, 0.0, ase3) // #22 
atom(<  0.92,   2.53,  -4.48>, 0.56, rgb <1.00, 0.05, 0.05>, 0.0, ase3) // #23 
atom(<  0.90,   2.55,  -1.55>, 0.56, rgb <1.00, 0.05, 0.05>, 0.0, ase3) // #24 
atom(< -2.18,   3.24,  -4.48>, 0.56, rgb <1.00, 0.05, 0.05>, 0.0, ase3) // #25 
atom(< -2.20,   3.37,  -1.55>, 0.56, rgb <1.00, 0.05, 0.05>, 0.0, ase3) // #26 
atom(< -0.26,   4.71,  -3.10>, 0.56, rgb <1.00, 0.05, 0.05>, 0.0, ase3) // #27 
atom(< -0.26,   4.71,  -0.01>, 0.56, rgb <1.00, 0.05, 0.05>, 0.0, ase3) // #28 
atom(<  2.19,   4.64,  -3.11>, 0.56, rgb <1.00, 0.05, 0.05>, 0.0, ase3) // #29 
atom(<  2.19,   4.64,   0.00>, 0.56, rgb <1.00, 0.05, 0.05>, 0.0, ase3) // #30 
atom(< -2.20,   5.80,  -4.48>, 0.56, rgb <1.00, 0.05, 0.05>, 0.0, ase3) // #31 
atom(< -2.27,   5.84,  -1.55>, 0.56, rgb <1.00, 0.05, 0.05>, 0.0, ase3) // #32 
atom(< -2.23,  -4.99,  -4.48>, 1.20, rgb <0.09, 0.33, 0.53>, 0.0, ase3) // #33 
atom(< -2.23,  -4.99,  -1.55>, 1.20, rgb <0.09, 0.33, 0.53>, 0.0, ase3) // #34 
atom(<  0.93,  -4.99,  -3.01>, 1.20, rgb <0.09, 0.33, 0.53>, 0.0, ase3) // #35 
atom(<  0.93,  -4.99,  -0.09>, 1.20, rgb <0.09, 0.33, 0.53>, 0.0, ase3) // #36 
atom(< -2.23,  -1.83,  -3.01>, 1.20, rgb <0.09, 0.33, 0.53>, 0.0, ase3) // #37 
atom(< -2.23,  -1.83,  -0.09>, 1.20, rgb <0.09, 0.33, 0.53>, 0.0, ase3) // #38 
atom(<  0.93,  -1.83,  -4.48>, 1.20, rgb <0.09, 0.33, 0.53>, 0.0, ase3) // #39 
atom(<  0.93,  -1.83,  -1.55>, 1.20, rgb <0.09, 0.33, 0.53>, 0.0, ase3) // #40 
atom(< -2.23,   1.34,  -4.48>, 1.20, rgb <0.09, 0.33, 0.53>, 0.0, ase3) // #41 
atom(< -2.23,   1.38,  -1.55>, 1.20, rgb <0.09, 0.33, 0.53>, 0.0, ase3) // #42 
atom(<  0.93,   1.30,  -3.01>, 1.20, rgb <0.09, 0.33, 0.53>, 0.0, ase3) // #43 
atom(<  0.93,   1.30,  -0.10>, 1.20, rgb <0.09, 0.33, 0.53>, 0.0, ase3) // #44 
atom(< -2.20,   4.59,  -3.09>, 1.20, rgb <0.09, 0.33, 0.53>, 0.0, ase3) // #45 
atom(< -2.20,   4.59,  -0.02>, 1.20, rgb <0.09, 0.33, 0.53>, 0.0, ase3) // #46 
atom(<  0.96,   4.37,  -4.48>, 1.20, rgb <0.09, 0.33, 0.53>, 0.0, ase3) // #47 
atom(<  0.97,   4.50,  -1.55>, 1.02, rgb <0.40, 0.56, 0.56>, 0.0, ase3) // #48 
cylinder {< -2.27,   5.84,  -1.55>, < -1.92,   6.18,  -1.55>, Rbond texture{pigment {color rgb <1.00, 0.05, 0.05> transmit 0.0} finish{ase3}}}
cylinder {< -1.57,   6.51,  -1.55>, < -1.92,   6.18,  -1.55>, Rbond texture{pigment {color rgb <1.00, 1.00, 1.00> transmit 0.0} finish{ase3}}}
cylinder {< -2.23,  -4.99,  -4.48>, < -1.61,  -4.99,  -3.75>, Rbond texture{pigment {color rgb <0.09, 0.33, 0.53> transmit 0.0} finish{ase3}}}
cylinder {< -1.00,  -4.99,  -3.01>, < -1.61,  -4.99,  -3.75>, Rbond texture{pigment {color rgb <1.00, 0.05, 0.05> transmit 0.0} finish{ase3}}}
cylinder {< -2.23,  -4.99,  -4.48>, < -2.23,  -4.02,  -4.48>, Rbond texture{pigment {color rgb <0.09, 0.33, 0.53> transmit 0.0} finish{ase3}}}
cylinder {< -2.23,  -3.06,  -4.48>, < -2.23,  -4.02,  -4.48>, Rbond texture{pigment {color rgb <1.00, 0.05, 0.05> transmit 0.0} finish{ase3}}}
cylinder {< -2.23,  -4.99,  -1.55>, < -1.61,  -4.99,  -2.28>, Rbond texture{pigment {color rgb <0.09, 0.33, 0.53> transmit 0.0} finish{ase3}}}
cylinder {< -1.00,  -4.99,  -3.01>, < -1.61,  -4.99,  -2.28>, Rbond texture{pigment {color rgb <1.00, 0.05, 0.05> transmit 0.0} finish{ase3}}}
cylinder {< -2.23,  -4.99,  -1.55>, < -1.61,  -4.99,  -0.82>, Rbond texture{pigment {color rgb <0.09, 0.33, 0.53> transmit 0.0} finish{ase3}}}
cylinder {< -1.00,  -4.99,  -0.09>, < -1.61,  -4.99,  -0.82>, Rbond texture{pigment {color rgb <1.00, 0.05, 0.05> transmit 0.0} finish{ase3}}}
cylinder {< -2.23,  -4.99,  -1.55>, < -2.23,  -4.02,  -1.55>, Rbond texture{pigment {color rgb <0.09, 0.33, 0.53> transmit 0.0} finish{ase3}}}
cylinder {< -2.23,  -3.06,  -1.55>, < -2.23,  -4.02,  -1.55>, Rbond texture{pigment {color rgb <1.00, 0.05, 0.05> transmit 0.0} finish{ase3}}}
cylinder {<  0.93,  -4.99,  -3.01>, <  0.93,  -5.60,  -3.75>, Rbond texture{pigment {color rgb <0.09, 0.33, 0.53> transmit 0.0} finish{ase3}}}
cylinder {<  0.93,  -6.22,  -4.48>, <  0.93,  -5.60,  -3.75>, Rbond texture{pigment {color rgb <1.00, 0.05, 0.05> transmit 0.0} finish{ase3}}}
cylinder {<  0.93,  -4.99,  -3.01>, <  0.93,  -5.60,  -2.28>, Rbond texture{pigment {color rgb <0.09, 0.33, 0.53> transmit 0.0} finish{ase3}}}
cylinder {<  0.93,  -6.22,  -1.55>, <  0.93,  -5.60,  -2.28>, Rbond texture{pigment {color rgb <1.00, 0.05, 0.05> transmit 0.0} finish{ase3}}}
cylinder {<  0.93,  -4.99,  -3.01>, < -0.03,  -4.99,  -3.01>, Rbond texture{pigment {color rgb <0.09, 0.33, 0.53> transmit 0.0} finish{ase3}}}
cylinder {< -1.00,  -4.99,  -3.01>, < -0.03,  -4.99,  -3.01>, Rbond texture{pigment {color rgb <1.00, 0.05, 0.05> transmit 0.0} finish{ase3}}}
cylinder {<  0.93,  -4.99,  -3.01>, <  1.90,  -4.99,  -3.01>, Rbond texture{pigment {color rgb <0.09, 0.33, 0.53> transmit 0.0} finish{ase3}}}
cylinder {<  2.87,  -4.99,  -3.01>, <  1.90,  -4.99,  -3.01>, Rbond texture{pigment {color rgb <1.00, 0.05, 0.05> transmit 0.0} finish{ase3}}}
cylinder {<  0.93,  -4.99,  -3.01>, <  0.93,  -4.38,  -3.75>, Rbond texture{pigment {color rgb <0.09, 0.33, 0.53> transmit 0.0} finish{ase3}}}
cylinder {<  0.93,  -3.76,  -4.48>, <  0.93,  -4.38,  -3.75>, Rbond texture{pigment {color rgb <1.00, 0.05, 0.05> transmit 0.0} finish{ase3}}}
cylinder {<  0.93,  -4.99,  -3.01>, <  0.93,  -4.38,  -2.28>, Rbond texture{pigment {color rgb <0.09, 0.33, 0.53> transmit 0.0} finish{ase3}}}
cylinder {<  0.93,  -3.76,  -1.55>, <  0.93,  -4.38,  -2.28>, Rbond texture{pigment {color rgb <1.00, 0.05, 0.05> transmit 0.0} finish{ase3}}}
cylinder {<  0.93,  -4.99,  -0.09>, <  0.93,  -5.60,  -0.82>, Rbond texture{pigment {color rgb <0.09, 0.33, 0.53> transmit 0.0} finish{ase3}}}
cylinder {<  0.93,  -6.22,  -1.55>, <  0.93,  -5.60,  -0.82>, Rbond texture{pigment {color rgb <1.00, 0.05, 0.05> transmit 0.0} finish{ase3}}}
cylinder {<  0.93,  -4.99,  -0.09>, < -0.03,  -4.99,  -0.09>, Rbond texture{pigment {color rgb <0.09, 0.33, 0.53> transmit 0.0} finish{ase3}}}
cylinder {< -1.00,  -4.99,  -0.09>, < -0.03,  -4.99,  -0.09>, Rbond texture{pigment {color rgb <1.00, 0.05, 0.05> transmit 0.0} finish{ase3}}}
cylinder {<  0.93,  -4.99,  -0.09>, <  1.90,  -4.99,  -0.09>, Rbond texture{pigment {color rgb <0.09, 0.33, 0.53> transmit 0.0} finish{ase3}}}
cylinder {<  2.87,  -4.99,  -0.09>, <  1.90,  -4.99,  -0.09>, Rbond texture{pigment {color rgb <1.00, 0.05, 0.05> transmit 0.0} finish{ase3}}}
cylinder {<  0.93,  -4.99,  -0.09>, <  0.93,  -4.38,  -0.82>, Rbond texture{pigment {color rgb <0.09, 0.33, 0.53> transmit 0.0} finish{ase3}}}
cylinder {<  0.93,  -3.76,  -1.55>, <  0.93,  -4.38,  -0.82>, Rbond texture{pigment {color rgb <1.00, 0.05, 0.05> transmit 0.0} finish{ase3}}}
cylinder {< -2.23,  -1.83,  -3.01>, < -2.23,  -2.44,  -3.75>, Rbond texture{pigment {color rgb <0.09, 0.33, 0.53> transmit 0.0} finish{ase3}}}
cylinder {< -2.23,  -3.06,  -4.48>, < -2.23,  -2.44,  -3.75>, Rbond texture{pigment {color rgb <1.00, 0.05, 0.05> transmit 0.0} finish{ase3}}}
cylinder {< -2.23,  -1.83,  -3.01>, < -2.23,  -2.44,  -2.28>, Rbond texture{pigment {color rgb <0.09, 0.33, 0.53> transmit 0.0} finish{ase3}}}
cylinder {< -2.23,  -3.06,  -1.55>, < -2.23,  -2.44,  -2.28>, Rbond texture{pigment {color rgb <1.00, 0.05, 0.05> transmit 0.0} finish{ase3}}}
cylinder {< -2.23,  -1.83,  -3.01>, < -1.26,  -1.83,  -3.01>, Rbond texture{pigment {color rgb <0.09, 0.33, 0.53> transmit 0.0} finish{ase3}}}
cylinder {< -0.29,  -1.83,  -3.01>, < -1.26,  -1.83,  -3.01>, Rbond texture{pigment {color rgb <1.00, 0.05, 0.05> transmit 0.0} finish{ase3}}}
cylinder {< -2.23,  -1.83,  -3.01>, < -2.23,  -1.22,  -3.75>, Rbond texture{pigment {color rgb <0.09, 0.33, 0.53> transmit 0.0} finish{ase3}}}
cylinder {< -2.23,  -0.61,  -4.48>, < -2.23,  -1.22,  -3.75>, Rbond texture{pigment {color rgb <1.00, 0.05, 0.05> transmit 0.0} finish{ase3}}}
cylinder {< -2.23,  -1.83,  -3.01>, < -2.23,  -1.22,  -2.28>, Rbond texture{pigment {color rgb <0.09, 0.33, 0.53> transmit 0.0} finish{ase3}}}
cylinder {< -2.23,  -0.61,  -1.55>, < -2.23,  -1.22,  -2.28>, Rbond texture{pigment {color rgb <1.00, 0.05, 0.05> transmit 0.0} finish{ase3}}}
cylinder {< -2.23,  -1.83,  -0.09>, < -2.23,  -2.44,  -0.82>, Rbond texture{pigment {color rgb <0.09, 0.33, 0.53> transmit 0.0} finish{ase3}}}
cylinder {< -2.23,  -3.06,  -1.55>, < -2.23,  -2.44,  -0.82>, Rbond texture{pigment {color rgb <1.00, 0.05, 0.05> transmit 0.0} finish{ase3}}}
cylinder {< -2.23,  -1.83,  -0.09>, < -1.26,  -1.83,  -0.09>, Rbond texture{pigment {color rgb <0.09, 0.33, 0.53> transmit 0.0} finish{ase3}}}
cylinder {< -0.29,  -1.83,  -0.09>, < -1.26,  -1.83,  -0.09>, Rbond texture{pigment {color rgb <1.00, 0.05, 0.05> transmit 0.0} finish{ase3}}}
cylinder {< -2.23,  -1.83,  -0.09>, < -2.23,  -1.22,  -0.82>, Rbond texture{pigment {color rgb <0.09, 0.33, 0.53> transmit 0.0} finish{ase3}}}
cylinder {< -2.23,  -0.61,  -1.55>, < -2.23,  -1.22,  -0.82>, Rbond texture{pigment {color rgb <1.00, 0.05, 0.05> transmit 0.0} finish{ase3}}}
cylinder {<  0.93,  -1.83,  -4.48>, <  0.93,  -2.80,  -4.48>, Rbond texture{pigment {color rgb <0.09, 0.33, 0.53> transmit 0.0} finish{ase3}}}
cylinder {<  0.93,  -3.76,  -4.48>, <  0.93,  -2.80,  -4.48>, Rbond texture{pigment {color rgb <1.00, 0.05, 0.05> transmit 0.0} finish{ase3}}}
cylinder {<  0.93,  -1.83,  -4.48>, <  0.32,  -1.83,  -3.75>, Rbond texture{pigment {color rgb <0.09, 0.33, 0.53> transmit 0.0} finish{ase3}}}
cylinder {< -0.29,  -1.83,  -3.01>, <  0.32,  -1.83,  -3.75>, Rbond texture{pigment {color rgb <1.00, 0.05, 0.05> transmit 0.0} finish{ase3}}}
cylinder {<  0.93,  -1.83,  -4.48>, <  1.54,  -1.83,  -3.75>, Rbond texture{pigment {color rgb <0.09, 0.33, 0.53> transmit 0.0} finish{ase3}}}
cylinder {<  2.16,  -1.83,  -3.01>, <  1.54,  -1.83,  -3.75>, Rbond texture{pigment {color rgb <1.00, 0.05, 0.05> transmit 0.0} finish{ase3}}}
cylinder {<  0.93,  -1.83,  -4.48>, <  0.93,  -0.87,  -4.48>, Rbond texture{pigment {color rgb <0.09, 0.33, 0.53> transmit 0.0} finish{ase3}}}
cylinder {<  0.93,   0.10,  -4.48>, <  0.93,  -0.87,  -4.48>, Rbond texture{pigment {color rgb <1.00, 0.05, 0.05> transmit 0.0} finish{ase3}}}
cylinder {<  0.93,  -1.83,  -1.55>, <  0.93,  -2.80,  -1.55>, Rbond texture{pigment {color rgb <0.09, 0.33, 0.53> transmit 0.0} finish{ase3}}}
cylinder {<  0.93,  -3.76,  -1.55>, <  0.93,  -2.80,  -1.55>, Rbond texture{pigment {color rgb <1.00, 0.05, 0.05> transmit 0.0} finish{ase3}}}
cylinder {<  0.93,  -1.83,  -1.55>, <  0.32,  -1.83,  -2.28>, Rbond texture{pigment {color rgb <0.09, 0.33, 0.53> transmit 0.0} finish{ase3}}}
cylinder {< -0.29,  -1.83,  -3.01>, <  0.32,  -1.83,  -2.28>, Rbond texture{pigment {color rgb <1.00, 0.05, 0.05> transmit 0.0} finish{ase3}}}
cylinder {<  0.93,  -1.83,  -1.55>, <  0.32,  -1.83,  -0.82>, Rbond texture{pigment {color rgb <0.09, 0.33, 0.53> transmit 0.0} finish{ase3}}}
cylinder {< -0.29,  -1.83,  -0.09>, <  0.32,  -1.83,  -0.82>, Rbond texture{pigment {color rgb <1.00, 0.05, 0.05> transmit 0.0} finish{ase3}}}
cylinder {<  0.93,  -1.83,  -1.55>, <  1.54,  -1.83,  -2.28>, Rbond texture{pigment {color rgb <0.09, 0.33, 0.53> transmit 0.0} finish{ase3}}}
cylinder {<  2.16,  -1.83,  -3.01>, <  1.54,  -1.83,  -2.28>, Rbond texture{pigment {color rgb <1.00, 0.05, 0.05> transmit 0.0} finish{ase3}}}
cylinder {<  0.93,  -1.83,  -1.55>, <  1.54,  -1.83,  -0.82>, Rbond texture{pigment {color rgb <0.09, 0.33, 0.53> transmit 0.0} finish{ase3}}}
cylinder {<  2.16,  -1.83,  -0.09>, <  1.54,  -1.83,  -0.82>, Rbond texture{pigment {color rgb <1.00, 0.05, 0.05> transmit 0.0} finish{ase3}}}
cylinder {<  0.93,  -1.83,  -1.55>, <  0.93,  -0.86,  -1.55>, Rbond texture{pigment {color rgb <0.09, 0.33, 0.53> transmit 0.0} finish{ase3}}}
cylinder {<  0.93,   0.11,  -1.55>, <  0.93,  -0.86,  -1.55>, Rbond texture{pigment {color rgb <1.00, 0.05, 0.05> transmit 0.0} finish{ase3}}}
cylinder {< -2.23,   1.34,  -4.48>, < -2.23,   0.37,  -4.48>, Rbond texture{pigment {color rgb <0.09, 0.33, 0.53> transmit 0.0} finish{ase3}}}
cylinder {< -2.23,  -0.61,  -4.48>, < -2.23,   0.37,  -4.48>, Rbond texture{pigment {color rgb <1.00, 0.05, 0.05> transmit 0.0} finish{ase3}}}
cylinder {< -2.23,   1.34,  -4.48>, < -1.62,   1.34,  -3.74>, Rbond texture{pigment {color rgb <0.09, 0.33, 0.53> transmit 0.0} finish{ase3}}}
cylinder {< -1.00,   1.33,  -3.01>, < -1.62,   1.34,  -3.74>, Rbond texture{pigment {color rgb <1.00, 0.05, 0.05> transmit 0.0} finish{ase3}}}
cylinder {< -2.23,   1.34,  -4.48>, < -2.21,   2.29,  -4.48>, Rbond texture{pigment {color rgb <0.09, 0.33, 0.53> transmit 0.0} finish{ase3}}}
cylinder {< -2.18,   3.24,  -4.48>, < -2.21,   2.29,  -4.48>, Rbond texture{pigment {color rgb <1.00, 0.05, 0.05> transmit 0.0} finish{ase3}}}
cylinder {< -2.23,   1.38,  -1.55>, < -2.23,   0.39,  -1.55>, Rbond texture{pigment {color rgb <0.09, 0.33, 0.53> transmit 0.0} finish{ase3}}}
cylinder {< -2.23,  -0.61,  -1.55>, < -2.23,   0.39,  -1.55>, Rbond texture{pigment {color rgb <1.00, 0.05, 0.05> transmit 0.0} finish{ase3}}}
cylinder {< -2.23,   1.38,  -1.55>, < -1.62,   1.35,  -2.28>, Rbond texture{pigment {color rgb <0.09, 0.33, 0.53> transmit 0.0} finish{ase3}}}
cylinder {< -1.00,   1.33,  -3.01>, < -1.62,   1.35,  -2.28>, Rbond texture{pigment {color rgb <1.00, 0.05, 0.05> transmit 0.0} finish{ase3}}}
cylinder {< -2.23,   1.38,  -1.55>, < -1.62,   1.35,  -0.83>, Rbond texture{pigment {color rgb <0.09, 0.33, 0.53> transmit 0.0} finish{ase3}}}
cylinder {< -1.00,   1.33,  -0.10>, < -1.62,   1.35,  -0.83>, Rbond texture{pigment {color rgb <1.00, 0.05, 0.05> transmit 0.0} finish{ase3}}}
cylinder {< -2.23,   1.38,  -1.55>, < -2.21,   2.38,  -1.55>, Rbond texture{pigment {color rgb <0.09, 0.33, 0.53> transmit 0.0} finish{ase3}}}
cylinder {< -2.20,   3.37,  -1.55>, < -2.21,   2.38,  -1.55>, Rbond texture{pigment {color rgb <1.00, 0.05, 0.05> transmit 0.0} finish{ase3}}}
cylinder {<  0.93,   1.30,  -3.01>, <  0.93,   0.70,  -3.74>, Rbond texture{pigment {color rgb <0.09, 0.33, 0.53> transmit 0.0} finish{ase3}}}
cylinder {<  0.93,   0.10,  -4.48>, <  0.93,   0.70,  -3.74>, Rbond texture{pigment {color rgb <1.00, 0.05, 0.05> transmit 0.0} finish{ase3}}}
cylinder {<  0.93,   1.30,  -3.01>, <  0.93,   0.70,  -2.28>, Rbond texture{pigment {color rgb <0.09, 0.33, 0.53> transmit 0.0} finish{ase3}}}
cylinder {<  0.93,   0.11,  -1.55>, <  0.93,   0.70,  -2.28>, Rbond texture{pigment {color rgb <1.00, 0.05, 0.05> transmit 0.0} finish{ase3}}}
cylinder {<  0.93,   1.30,  -3.01>, < -0.04,   1.31,  -3.01>, Rbond texture{pigment {color rgb <0.09, 0.33, 0.53> transmit 0.0} finish{ase3}}}
cylinder {< -1.00,   1.33,  -3.01>, < -0.04,   1.31,  -3.01>, Rbond texture{pigment {color rgb <1.00, 0.05, 0.05> transmit 0.0} finish{ase3}}}
cylinder {<  0.93,   1.30,  -3.01>, <  1.89,   1.33,  -3.01>, Rbond texture{pigment {color rgb <0.09, 0.33, 0.53> transmit 0.0} finish{ase3}}}
cylinder {<  2.86,   1.36,  -3.01>, <  1.89,   1.33,  -3.01>, Rbond texture{pigment {color rgb <1.00, 0.05, 0.05> transmit 0.0} finish{ase3}}}
cylinder {<  0.93,   1.30,  -3.01>, <  0.92,   1.91,  -3.74>, Rbond texture{pigment {color rgb <0.09, 0.33, 0.53> transmit 0.0} finish{ase3}}}
cylinder {<  0.92,   2.53,  -4.48>, <  0.92,   1.91,  -3.74>, Rbond texture{pigment {color rgb <1.00, 0.05, 0.05> transmit 0.0} finish{ase3}}}
cylinder {<  0.93,   1.30,  -3.01>, <  0.91,   1.92,  -2.28>, Rbond texture{pigment {color rgb <0.09, 0.33, 0.53> transmit 0.0} finish{ase3}}}
cylinder {<  0.90,   2.55,  -1.55>, <  0.91,   1.92,  -2.28>, Rbond texture{pigment {color rgb <1.00, 0.05, 0.05> transmit 0.0} finish{ase3}}}
cylinder {<  0.93,   1.30,  -0.10>, <  0.93,   0.70,  -0.82>, Rbond texture{pigment {color rgb <0.09, 0.33, 0.53> transmit 0.0} finish{ase3}}}
cylinder {<  0.93,   0.11,  -1.55>, <  0.93,   0.70,  -0.82>, Rbond texture{pigment {color rgb <1.00, 0.05, 0.05> transmit 0.0} finish{ase3}}}
cylinder {<  0.93,   1.30,  -0.10>, < -0.04,   1.31,  -0.10>, Rbond texture{pigment {color rgb <0.09, 0.33, 0.53> transmit 0.0} finish{ase3}}}
cylinder {< -1.00,   1.33,  -0.10>, < -0.04,   1.31,  -0.10>, Rbond texture{pigment {color rgb <1.00, 0.05, 0.05> transmit 0.0} finish{ase3}}}
cylinder {<  0.93,   1.30,  -0.10>, <  1.89,   1.33,  -0.10>, Rbond texture{pigment {color rgb <0.09, 0.33, 0.53> transmit 0.0} finish{ase3}}}
cylinder {<  2.86,   1.36,  -0.10>, <  1.89,   1.33,  -0.10>, Rbond texture{pigment {color rgb <1.00, 0.05, 0.05> transmit 0.0} finish{ase3}}}
cylinder {<  0.93,   1.30,  -0.10>, <  0.91,   1.92,  -0.82>, Rbond texture{pigment {color rgb <0.09, 0.33, 0.53> transmit 0.0} finish{ase3}}}
cylinder {<  0.90,   2.55,  -1.55>, <  0.91,   1.92,  -0.82>, Rbond texture{pigment {color rgb <1.00, 0.05, 0.05> transmit 0.0} finish{ase3}}}
cylinder {< -2.20,   4.59,  -3.09>, < -2.19,   3.91,  -3.78>, Rbond texture{pigment {color rgb <0.09, 0.33, 0.53> transmit 0.0} finish{ase3}}}
cylinder {< -2.18,   3.24,  -4.48>, < -2.19,   3.91,  -3.78>, Rbond texture{pigment {color rgb <1.00, 0.05, 0.05> transmit 0.0} finish{ase3}}}
cylinder {< -2.20,   4.59,  -3.09>, < -2.20,   3.98,  -2.32>, Rbond texture{pigment {color rgb <0.09, 0.33, 0.53> transmit 0.0} finish{ase3}}}
cylinder {< -2.20,   3.37,  -1.55>, < -2.20,   3.98,  -2.32>, Rbond texture{pigment {color rgb <1.00, 0.05, 0.05> transmit 0.0} finish{ase3}}}
cylinder {< -2.20,   4.59,  -3.09>, < -1.23,   4.65,  -3.09>, Rbond texture{pigment {color rgb <0.09, 0.33, 0.53> transmit 0.0} finish{ase3}}}
cylinder {< -0.26,   4.71,  -3.10>, < -1.23,   4.65,  -3.09>, Rbond texture{pigment {color rgb <1.00, 0.05, 0.05> transmit 0.0} finish{ase3}}}
cylinder {< -2.20,   4.59,  -3.09>, < -2.20,   5.19,  -3.78>, Rbond texture{pigment {color rgb <0.09, 0.33, 0.53> transmit 0.0} finish{ase3}}}
cylinder {< -2.20,   5.80,  -4.48>, < -2.20,   5.19,  -3.78>, Rbond texture{pigment {color rgb <1.00, 0.05, 0.05> transmit 0.0} finish{ase3}}}
cylinder {< -2.20,   4.59,  -3.09>, < -2.23,   5.21,  -2.32>, Rbond texture{pigment {color rgb <0.09, 0.33, 0.53> transmit 0.0} finish{ase3}}}
cylinder {< -2.27,   5.84,  -1.55>, < -2.23,   5.21,  -2.32>, Rbond texture{pigment {color rgb <1.00, 0.05, 0.05> transmit 0.0} finish{ase3}}}
cylinder {< -2.20,   4.59,  -0.02>, < -2.20,   3.98,  -0.79>, Rbond texture{pigment {color rgb <0.09, 0.33, 0.53> transmit 0.0} finish{ase3}}}
cylinder {< -2.20,   3.37,  -1.55>, < -2.20,   3.98,  -0.79>, Rbond texture{pigment {color rgb <1.00, 0.05, 0.05> transmit 0.0} finish{ase3}}}
cylinder {< -2.20,   4.59,  -0.02>, < -1.23,   4.65,  -0.01>, Rbond texture{pigment {color rgb <0.09, 0.33, 0.53> transmit 0.0} finish{ase3}}}
cylinder {< -0.26,   4.71,  -0.01>, < -1.23,   4.65,  -0.01>, Rbond texture{pigment {color rgb <1.00, 0.05, 0.05> transmit 0.0} finish{ase3}}}
cylinder {< -2.20,   4.59,  -0.02>, < -2.23,   5.21,  -0.79>, Rbond texture{pigment {color rgb <0.09, 0.33, 0.53> transmit 0.0} finish{ase3}}}
cylinder {< -2.27,   5.84,  -1.55>, < -2.23,   5.21,  -0.79>, Rbond texture{pigment {color rgb <1.00, 0.05, 0.05> transmit 0.0} finish{ase3}}}
cylinder {<  0.96,   4.37,  -4.48>, <  0.94,   3.45,  -4.48>, Rbond texture{pigment {color rgb <0.09, 0.33, 0.53> transmit 0.0} finish{ase3}}}
cylinder {<  0.92,   2.53,  -4.48>, <  0.94,   3.45,  -4.48>, Rbond texture{pigment {color rgb <1.00, 0.05, 0.05> transmit 0.0} finish{ase3}}}
cylinder {<  0.96,   4.37,  -4.48>, <  0.35,   4.54,  -3.79>, Rbond texture{pigment {color rgb <0.09, 0.33, 0.53> transmit 0.0} finish{ase3}}}
cylinder {< -0.26,   4.71,  -3.10>, <  0.35,   4.54,  -3.79>, Rbond texture{pigment {color rgb <1.00, 0.05, 0.05> transmit 0.0} finish{ase3}}}
cylinder {<  0.96,   4.37,  -4.48>, <  1.58,   4.51,  -3.79>, Rbond texture{pigment {color rgb <0.09, 0.33, 0.53> transmit 0.0} finish{ase3}}}
cylinder {<  2.19,   4.64,  -3.11>, <  1.58,   4.51,  -3.79>, Rbond texture{pigment {color rgb <1.00, 0.05, 0.05> transmit 0.0} finish{ase3}}}
cylinder {<  0.97,   4.50,  -1.55>, <  0.94,   3.53,  -1.55>, Rbond texture{pigment {color rgb <0.40, 0.56, 0.56> transmit 0.0} finish{ase3}}}
cylinder {<  0.90,   2.55,  -1.55>, <  0.94,   3.53,  -1.55>, Rbond texture{pigment {color rgb <1.00, 0.05, 0.05> transmit 0.0} finish{ase3}}}
cylinder {<  0.97,   4.50,  -1.55>, <  0.35,   4.61,  -2.33>, Rbond texture{pigment {color rgb <0.40, 0.56, 0.56> transmit 0.0} finish{ase3}}}
cylinder {< -0.26,   4.71,  -3.10>, <  0.35,   4.61,  -2.33>, Rbond texture{pigment {color rgb <1.00, 0.05, 0.05> transmit 0.0} finish{ase3}}}
cylinder {<  0.97,   4.50,  -1.55>, <  0.35,   4.61,  -0.78>, Rbond texture{pigment {color rgb <0.40, 0.56, 0.56> transmit 0.0} finish{ase3}}}
cylinder {< -0.26,   4.71,  -0.01>, <  0.35,   4.61,  -0.78>, Rbond texture{pigment {color rgb <1.00, 0.05, 0.05> transmit 0.0} finish{ase3}}}
cylinder {<  0.97,   4.50,  -1.55>, <  1.58,   4.57,  -2.33>, Rbond texture{pigment {color rgb <0.40, 0.56, 0.56> transmit 0.0} finish{ase3}}}
cylinder {<  2.19,   4.64,  -3.11>, <  1.58,   4.57,  -2.33>, Rbond texture{pigment {color rgb <1.00, 0.05, 0.05> transmit 0.0} finish{ase3}}}
cylinder {<  0.97,   4.50,  -1.55>, <  1.58,   4.57,  -0.78>, Rbond texture{pigment {color rgb <0.40, 0.56, 0.56> transmit 0.0} finish{ase3}}}
cylinder {<  2.19,   4.64,   0.00>, <  1.58,   4.57,  -0.78>, Rbond texture{pigment {color rgb <1.00, 0.05, 0.05> transmit 0.0} finish{ase3}}}
