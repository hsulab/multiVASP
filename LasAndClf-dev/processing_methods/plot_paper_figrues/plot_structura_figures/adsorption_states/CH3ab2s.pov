#include "colors.inc"
#include "finish.inc"

global_settings {assumed_gamma 1 max_trace_level 6}
background {color White}
camera {perspective
  right -7.20*x up 14.93*y
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

atom(<  0.93,   6.80,  -2.58>, 0.26, rgb <1.00, 1.00, 1.00>, 0.0, ase3) // #0 
atom(<  0.02,   6.79,  -1.03>, 0.26, rgb <1.00, 1.00, 1.00>, 0.0, ase3) // #1 
atom(<  1.85,   6.79,  -1.03>, 0.26, rgb <1.00, 1.00, 1.00>, 0.0, ase3) // #2 
atom(<  0.93,   6.46,  -1.54>, 0.65, rgb <0.56, 0.56, 0.56>, 0.0, ase3) // #3 
atom(<  0.93,  -6.55,  -4.46>, 0.56, rgb <1.00, 0.05, 0.05>, 0.0, ase3) // #4 
atom(<  0.93,  -6.55,  -1.53>, 0.56, rgb <1.00, 0.05, 0.05>, 0.0, ase3) // #5 
atom(< -1.00,  -5.32,  -2.99>, 0.56, rgb <1.00, 0.05, 0.05>, 0.0, ase3) // #6 
atom(< -1.00,  -5.32,  -0.07>, 0.56, rgb <1.00, 0.05, 0.05>, 0.0, ase3) // #7 
atom(<  2.87,  -5.32,  -2.99>, 0.56, rgb <1.00, 0.05, 0.05>, 0.0, ase3) // #8 
atom(<  2.87,  -5.32,  -0.07>, 0.56, rgb <1.00, 0.05, 0.05>, 0.0, ase3) // #9 
atom(<  0.93,  -4.10,  -4.46>, 0.56, rgb <1.00, 0.05, 0.05>, 0.0, ase3) // #10 
atom(<  0.93,  -4.10,  -1.53>, 0.56, rgb <1.00, 0.05, 0.05>, 0.0, ase3) // #11 
atom(< -2.23,  -3.39,  -4.46>, 0.56, rgb <1.00, 0.05, 0.05>, 0.0, ase3) // #12 
atom(< -2.23,  -3.39,  -1.53>, 0.56, rgb <1.00, 0.05, 0.05>, 0.0, ase3) // #13 
atom(< -0.29,  -2.16,  -2.99>, 0.56, rgb <1.00, 0.05, 0.05>, 0.0, ase3) // #14 
atom(< -0.29,  -2.16,  -0.07>, 0.56, rgb <1.00, 0.05, 0.05>, 0.0, ase3) // #15 
atom(<  2.16,  -2.16,  -2.99>, 0.56, rgb <1.00, 0.05, 0.05>, 0.0, ase3) // #16 
atom(<  2.16,  -2.16,  -0.07>, 0.56, rgb <1.00, 0.05, 0.05>, 0.0, ase3) // #17 
atom(< -2.23,  -0.94,  -4.46>, 0.56, rgb <1.00, 0.05, 0.05>, 0.0, ase3) // #18 
atom(< -2.23,  -0.94,  -1.53>, 0.56, rgb <1.00, 0.05, 0.05>, 0.0, ase3) // #19 
atom(<  0.93,  -0.23,  -4.45>, 0.56, rgb <1.00, 0.05, 0.05>, 0.0, ase3) // #20 
atom(<  0.93,  -0.26,  -1.53>, 0.56, rgb <1.00, 0.05, 0.05>, 0.0, ase3) // #21 
atom(< -1.00,   0.99,  -2.99>, 0.56, rgb <1.00, 0.05, 0.05>, 0.0, ase3) // #22 
atom(< -1.00,   0.99,  -0.07>, 0.56, rgb <1.00, 0.05, 0.05>, 0.0, ase3) // #23 
atom(<  2.86,   0.99,  -2.99>, 0.56, rgb <1.00, 0.05, 0.05>, 0.0, ase3) // #24 
atom(<  2.86,   1.00,  -0.07>, 0.56, rgb <1.00, 0.05, 0.05>, 0.0, ase3) // #25 
atom(<  0.93,   2.17,  -4.45>, 0.56, rgb <1.00, 0.05, 0.05>, 0.0, ase3) // #26 
atom(<  0.93,   2.20,  -1.53>, 0.56, rgb <1.00, 0.05, 0.05>, 0.0, ase3) // #27 
atom(< -2.23,   2.97,  -4.45>, 0.56, rgb <1.00, 0.05, 0.05>, 0.0, ase3) // #28 
atom(< -2.23,   2.97,  -1.53>, 0.56, rgb <1.00, 0.05, 0.05>, 0.0, ase3) // #29 
atom(< -0.26,   4.32,  -3.06>, 0.56, rgb <1.00, 0.05, 0.05>, 0.0, ase3) // #30 
atom(< -0.26,   4.32,  -0.00>, 0.56, rgb <1.00, 0.05, 0.05>, 0.0, ase3) // #31 
atom(<  2.13,   4.32,  -3.06>, 0.56, rgb <1.00, 0.05, 0.05>, 0.0, ase3) // #32 
atom(<  2.13,   4.32,   0.00>, 0.56, rgb <1.00, 0.05, 0.05>, 0.0, ase3) // #33 
atom(< -2.23,   5.46,  -4.45>, 0.56, rgb <1.00, 0.05, 0.05>, 0.0, ase3) // #34 
atom(< -2.23,   5.44,  -1.52>, 0.56, rgb <1.00, 0.05, 0.05>, 0.0, ase3) // #35 
atom(< -2.23,  -5.32,  -4.46>, 1.20, rgb <0.09, 0.33, 0.53>, 0.0, ase3) // #36 
atom(< -2.23,  -5.32,  -1.53>, 1.20, rgb <0.09, 0.33, 0.53>, 0.0, ase3) // #37 
atom(<  0.93,  -5.32,  -2.99>, 1.20, rgb <0.09, 0.33, 0.53>, 0.0, ase3) // #38 
atom(<  0.93,  -5.32,  -0.07>, 1.20, rgb <0.09, 0.33, 0.53>, 0.0, ase3) // #39 
atom(< -2.23,  -2.16,  -2.99>, 1.20, rgb <0.09, 0.33, 0.53>, 0.0, ase3) // #40 
atom(< -2.23,  -2.16,  -0.07>, 1.20, rgb <0.09, 0.33, 0.53>, 0.0, ase3) // #41 
atom(<  0.93,  -2.16,  -4.46>, 1.20, rgb <0.09, 0.33, 0.53>, 0.0, ase3) // #42 
atom(<  0.93,  -2.16,  -1.53>, 1.20, rgb <0.09, 0.33, 0.53>, 0.0, ase3) // #43 
atom(< -2.23,   1.04,  -4.45>, 1.20, rgb <0.09, 0.33, 0.53>, 0.0, ase3) // #44 
atom(< -2.23,   1.05,  -1.53>, 1.20, rgb <0.09, 0.33, 0.53>, 0.0, ase3) // #45 
atom(<  0.93,   0.96,  -2.96>, 1.20, rgb <0.09, 0.33, 0.53>, 0.0, ase3) // #46 
atom(<  0.93,   0.96,  -0.10>, 1.20, rgb <0.09, 0.33, 0.53>, 0.0, ase3) // #47 
atom(< -2.23,   4.32,  -2.99>, 1.20, rgb <0.09, 0.33, 0.53>, 0.0, ase3) // #48 
atom(< -2.23,   4.31,  -0.07>, 1.20, rgb <0.09, 0.33, 0.53>, 0.0, ase3) // #49 
atom(<  0.93,   3.97,  -4.45>, 1.20, rgb <0.09, 0.33, 0.53>, 0.0, ase3) // #50 
atom(<  0.93,   4.41,  -1.53>, 1.02, rgb <0.40, 0.56, 0.56>, 0.0, ase3) // #51 
cylinder {<  0.93,   6.46,  -1.54>, <  0.93,   6.63,  -2.06>, Rbond texture{pigment {color rgb <0.56, 0.56, 0.56> transmit 0.0} finish{ase3}}}
cylinder {<  0.93,   6.80,  -2.58>, <  0.93,   6.63,  -2.06>, Rbond texture{pigment {color rgb <1.00, 1.00, 1.00> transmit 0.0} finish{ase3}}}
cylinder {<  0.93,   6.46,  -1.54>, <  0.48,   6.63,  -1.28>, Rbond texture{pigment {color rgb <0.56, 0.56, 0.56> transmit 0.0} finish{ase3}}}
cylinder {<  0.02,   6.79,  -1.03>, <  0.48,   6.63,  -1.28>, Rbond texture{pigment {color rgb <1.00, 1.00, 1.00> transmit 0.0} finish{ase3}}}
cylinder {<  0.93,   6.46,  -1.54>, <  1.39,   6.63,  -1.28>, Rbond texture{pigment {color rgb <0.56, 0.56, 0.56> transmit 0.0} finish{ase3}}}
cylinder {<  1.85,   6.79,  -1.03>, <  1.39,   6.63,  -1.28>, Rbond texture{pigment {color rgb <1.00, 1.00, 1.00> transmit 0.0} finish{ase3}}}
cylinder {< -2.23,  -5.32,  -4.46>, < -1.62,  -5.32,  -3.72>, Rbond texture{pigment {color rgb <0.09, 0.33, 0.53> transmit 0.0} finish{ase3}}}
cylinder {< -1.00,  -5.32,  -2.99>, < -1.62,  -5.32,  -3.72>, Rbond texture{pigment {color rgb <1.00, 0.05, 0.05> transmit 0.0} finish{ase3}}}
cylinder {< -2.23,  -5.32,  -4.46>, < -2.23,  -4.35,  -4.46>, Rbond texture{pigment {color rgb <0.09, 0.33, 0.53> transmit 0.0} finish{ase3}}}
cylinder {< -2.23,  -3.39,  -4.46>, < -2.23,  -4.35,  -4.46>, Rbond texture{pigment {color rgb <1.00, 0.05, 0.05> transmit 0.0} finish{ase3}}}
cylinder {< -2.23,  -5.32,  -1.53>, < -1.62,  -5.32,  -2.26>, Rbond texture{pigment {color rgb <0.09, 0.33, 0.53> transmit 0.0} finish{ase3}}}
cylinder {< -1.00,  -5.32,  -2.99>, < -1.62,  -5.32,  -2.26>, Rbond texture{pigment {color rgb <1.00, 0.05, 0.05> transmit 0.0} finish{ase3}}}
cylinder {< -2.23,  -5.32,  -1.53>, < -1.62,  -5.32,  -0.80>, Rbond texture{pigment {color rgb <0.09, 0.33, 0.53> transmit 0.0} finish{ase3}}}
cylinder {< -1.00,  -5.32,  -0.07>, < -1.62,  -5.32,  -0.80>, Rbond texture{pigment {color rgb <1.00, 0.05, 0.05> transmit 0.0} finish{ase3}}}
cylinder {< -2.23,  -5.32,  -1.53>, < -2.23,  -4.35,  -1.53>, Rbond texture{pigment {color rgb <0.09, 0.33, 0.53> transmit 0.0} finish{ase3}}}
cylinder {< -2.23,  -3.39,  -1.53>, < -2.23,  -4.35,  -1.53>, Rbond texture{pigment {color rgb <1.00, 0.05, 0.05> transmit 0.0} finish{ase3}}}
cylinder {<  0.93,  -5.32,  -2.99>, <  0.93,  -5.93,  -3.72>, Rbond texture{pigment {color rgb <0.09, 0.33, 0.53> transmit 0.0} finish{ase3}}}
cylinder {<  0.93,  -6.55,  -4.46>, <  0.93,  -5.93,  -3.72>, Rbond texture{pigment {color rgb <1.00, 0.05, 0.05> transmit 0.0} finish{ase3}}}
cylinder {<  0.93,  -5.32,  -2.99>, <  0.93,  -5.93,  -2.26>, Rbond texture{pigment {color rgb <0.09, 0.33, 0.53> transmit 0.0} finish{ase3}}}
cylinder {<  0.93,  -6.55,  -1.53>, <  0.93,  -5.93,  -2.26>, Rbond texture{pigment {color rgb <1.00, 0.05, 0.05> transmit 0.0} finish{ase3}}}
cylinder {<  0.93,  -5.32,  -2.99>, < -0.04,  -5.32,  -2.99>, Rbond texture{pigment {color rgb <0.09, 0.33, 0.53> transmit 0.0} finish{ase3}}}
cylinder {< -1.00,  -5.32,  -2.99>, < -0.04,  -5.32,  -2.99>, Rbond texture{pigment {color rgb <1.00, 0.05, 0.05> transmit 0.0} finish{ase3}}}
cylinder {<  0.93,  -5.32,  -2.99>, <  1.90,  -5.32,  -2.99>, Rbond texture{pigment {color rgb <0.09, 0.33, 0.53> transmit 0.0} finish{ase3}}}
cylinder {<  2.87,  -5.32,  -2.99>, <  1.90,  -5.32,  -2.99>, Rbond texture{pigment {color rgb <1.00, 0.05, 0.05> transmit 0.0} finish{ase3}}}
cylinder {<  0.93,  -5.32,  -2.99>, <  0.93,  -4.71,  -3.72>, Rbond texture{pigment {color rgb <0.09, 0.33, 0.53> transmit 0.0} finish{ase3}}}
cylinder {<  0.93,  -4.10,  -4.46>, <  0.93,  -4.71,  -3.72>, Rbond texture{pigment {color rgb <1.00, 0.05, 0.05> transmit 0.0} finish{ase3}}}
cylinder {<  0.93,  -5.32,  -2.99>, <  0.93,  -4.71,  -2.26>, Rbond texture{pigment {color rgb <0.09, 0.33, 0.53> transmit 0.0} finish{ase3}}}
cylinder {<  0.93,  -4.10,  -1.53>, <  0.93,  -4.71,  -2.26>, Rbond texture{pigment {color rgb <1.00, 0.05, 0.05> transmit 0.0} finish{ase3}}}
cylinder {<  0.93,  -5.32,  -0.07>, <  0.93,  -5.93,  -0.80>, Rbond texture{pigment {color rgb <0.09, 0.33, 0.53> transmit 0.0} finish{ase3}}}
cylinder {<  0.93,  -6.55,  -1.53>, <  0.93,  -5.93,  -0.80>, Rbond texture{pigment {color rgb <1.00, 0.05, 0.05> transmit 0.0} finish{ase3}}}
cylinder {<  0.93,  -5.32,  -0.07>, < -0.04,  -5.32,  -0.07>, Rbond texture{pigment {color rgb <0.09, 0.33, 0.53> transmit 0.0} finish{ase3}}}
cylinder {< -1.00,  -5.32,  -0.07>, < -0.04,  -5.32,  -0.07>, Rbond texture{pigment {color rgb <1.00, 0.05, 0.05> transmit 0.0} finish{ase3}}}
cylinder {<  0.93,  -5.32,  -0.07>, <  1.90,  -5.32,  -0.07>, Rbond texture{pigment {color rgb <0.09, 0.33, 0.53> transmit 0.0} finish{ase3}}}
cylinder {<  2.87,  -5.32,  -0.07>, <  1.90,  -5.32,  -0.07>, Rbond texture{pigment {color rgb <1.00, 0.05, 0.05> transmit 0.0} finish{ase3}}}
cylinder {<  0.93,  -5.32,  -0.07>, <  0.93,  -4.71,  -0.80>, Rbond texture{pigment {color rgb <0.09, 0.33, 0.53> transmit 0.0} finish{ase3}}}
cylinder {<  0.93,  -4.10,  -1.53>, <  0.93,  -4.71,  -0.80>, Rbond texture{pigment {color rgb <1.00, 0.05, 0.05> transmit 0.0} finish{ase3}}}
cylinder {< -2.23,  -2.16,  -2.99>, < -2.23,  -2.78,  -3.72>, Rbond texture{pigment {color rgb <0.09, 0.33, 0.53> transmit 0.0} finish{ase3}}}
cylinder {< -2.23,  -3.39,  -4.46>, < -2.23,  -2.78,  -3.72>, Rbond texture{pigment {color rgb <1.00, 0.05, 0.05> transmit 0.0} finish{ase3}}}
cylinder {< -2.23,  -2.16,  -2.99>, < -2.23,  -2.78,  -2.26>, Rbond texture{pigment {color rgb <0.09, 0.33, 0.53> transmit 0.0} finish{ase3}}}
cylinder {< -2.23,  -3.39,  -1.53>, < -2.23,  -2.78,  -2.26>, Rbond texture{pigment {color rgb <1.00, 0.05, 0.05> transmit 0.0} finish{ase3}}}
cylinder {< -2.23,  -2.16,  -2.99>, < -1.26,  -2.16,  -2.99>, Rbond texture{pigment {color rgb <0.09, 0.33, 0.53> transmit 0.0} finish{ase3}}}
cylinder {< -0.29,  -2.16,  -2.99>, < -1.26,  -2.16,  -2.99>, Rbond texture{pigment {color rgb <1.00, 0.05, 0.05> transmit 0.0} finish{ase3}}}
cylinder {< -2.23,  -2.16,  -2.99>, < -2.23,  -1.55,  -3.72>, Rbond texture{pigment {color rgb <0.09, 0.33, 0.53> transmit 0.0} finish{ase3}}}
cylinder {< -2.23,  -0.94,  -4.46>, < -2.23,  -1.55,  -3.72>, Rbond texture{pigment {color rgb <1.00, 0.05, 0.05> transmit 0.0} finish{ase3}}}
cylinder {< -2.23,  -2.16,  -2.99>, < -2.23,  -1.55,  -2.26>, Rbond texture{pigment {color rgb <0.09, 0.33, 0.53> transmit 0.0} finish{ase3}}}
cylinder {< -2.23,  -0.94,  -1.53>, < -2.23,  -1.55,  -2.26>, Rbond texture{pigment {color rgb <1.00, 0.05, 0.05> transmit 0.0} finish{ase3}}}
cylinder {< -2.23,  -2.16,  -0.07>, < -2.23,  -2.78,  -0.80>, Rbond texture{pigment {color rgb <0.09, 0.33, 0.53> transmit 0.0} finish{ase3}}}
cylinder {< -2.23,  -3.39,  -1.53>, < -2.23,  -2.78,  -0.80>, Rbond texture{pigment {color rgb <1.00, 0.05, 0.05> transmit 0.0} finish{ase3}}}
cylinder {< -2.23,  -2.16,  -0.07>, < -1.26,  -2.16,  -0.07>, Rbond texture{pigment {color rgb <0.09, 0.33, 0.53> transmit 0.0} finish{ase3}}}
cylinder {< -0.29,  -2.16,  -0.07>, < -1.26,  -2.16,  -0.07>, Rbond texture{pigment {color rgb <1.00, 0.05, 0.05> transmit 0.0} finish{ase3}}}
cylinder {< -2.23,  -2.16,  -0.07>, < -2.23,  -1.55,  -0.80>, Rbond texture{pigment {color rgb <0.09, 0.33, 0.53> transmit 0.0} finish{ase3}}}
cylinder {< -2.23,  -0.94,  -1.53>, < -2.23,  -1.55,  -0.80>, Rbond texture{pigment {color rgb <1.00, 0.05, 0.05> transmit 0.0} finish{ase3}}}
cylinder {<  0.93,  -2.16,  -4.46>, <  0.93,  -3.13,  -4.46>, Rbond texture{pigment {color rgb <0.09, 0.33, 0.53> transmit 0.0} finish{ase3}}}
cylinder {<  0.93,  -4.10,  -4.46>, <  0.93,  -3.13,  -4.46>, Rbond texture{pigment {color rgb <1.00, 0.05, 0.05> transmit 0.0} finish{ase3}}}
cylinder {<  0.93,  -2.16,  -4.46>, <  0.32,  -2.16,  -3.72>, Rbond texture{pigment {color rgb <0.09, 0.33, 0.53> transmit 0.0} finish{ase3}}}
cylinder {< -0.29,  -2.16,  -2.99>, <  0.32,  -2.16,  -3.72>, Rbond texture{pigment {color rgb <1.00, 0.05, 0.05> transmit 0.0} finish{ase3}}}
cylinder {<  0.93,  -2.16,  -4.46>, <  1.54,  -2.16,  -3.72>, Rbond texture{pigment {color rgb <0.09, 0.33, 0.53> transmit 0.0} finish{ase3}}}
cylinder {<  2.16,  -2.16,  -2.99>, <  1.54,  -2.16,  -3.72>, Rbond texture{pigment {color rgb <1.00, 0.05, 0.05> transmit 0.0} finish{ase3}}}
cylinder {<  0.93,  -2.16,  -4.46>, <  0.93,  -1.20,  -4.45>, Rbond texture{pigment {color rgb <0.09, 0.33, 0.53> transmit 0.0} finish{ase3}}}
cylinder {<  0.93,  -0.23,  -4.45>, <  0.93,  -1.20,  -4.45>, Rbond texture{pigment {color rgb <1.00, 0.05, 0.05> transmit 0.0} finish{ase3}}}
cylinder {<  0.93,  -2.16,  -1.53>, <  0.93,  -3.13,  -1.53>, Rbond texture{pigment {color rgb <0.09, 0.33, 0.53> transmit 0.0} finish{ase3}}}
cylinder {<  0.93,  -4.10,  -1.53>, <  0.93,  -3.13,  -1.53>, Rbond texture{pigment {color rgb <1.00, 0.05, 0.05> transmit 0.0} finish{ase3}}}
cylinder {<  0.93,  -2.16,  -1.53>, <  0.32,  -2.16,  -2.26>, Rbond texture{pigment {color rgb <0.09, 0.33, 0.53> transmit 0.0} finish{ase3}}}
cylinder {< -0.29,  -2.16,  -2.99>, <  0.32,  -2.16,  -2.26>, Rbond texture{pigment {color rgb <1.00, 0.05, 0.05> transmit 0.0} finish{ase3}}}
cylinder {<  0.93,  -2.16,  -1.53>, <  0.32,  -2.16,  -0.80>, Rbond texture{pigment {color rgb <0.09, 0.33, 0.53> transmit 0.0} finish{ase3}}}
cylinder {< -0.29,  -2.16,  -0.07>, <  0.32,  -2.16,  -0.80>, Rbond texture{pigment {color rgb <1.00, 0.05, 0.05> transmit 0.0} finish{ase3}}}
cylinder {<  0.93,  -2.16,  -1.53>, <  1.54,  -2.16,  -2.26>, Rbond texture{pigment {color rgb <0.09, 0.33, 0.53> transmit 0.0} finish{ase3}}}
cylinder {<  2.16,  -2.16,  -2.99>, <  1.54,  -2.16,  -2.26>, Rbond texture{pigment {color rgb <1.00, 0.05, 0.05> transmit 0.0} finish{ase3}}}
cylinder {<  0.93,  -2.16,  -1.53>, <  1.54,  -2.16,  -0.80>, Rbond texture{pigment {color rgb <0.09, 0.33, 0.53> transmit 0.0} finish{ase3}}}
cylinder {<  2.16,  -2.16,  -0.07>, <  1.54,  -2.16,  -0.80>, Rbond texture{pigment {color rgb <1.00, 0.05, 0.05> transmit 0.0} finish{ase3}}}
cylinder {<  0.93,  -2.16,  -1.53>, <  0.93,  -1.21,  -1.53>, Rbond texture{pigment {color rgb <0.09, 0.33, 0.53> transmit 0.0} finish{ase3}}}
cylinder {<  0.93,  -0.26,  -1.53>, <  0.93,  -1.21,  -1.53>, Rbond texture{pigment {color rgb <1.00, 0.05, 0.05> transmit 0.0} finish{ase3}}}
cylinder {< -2.23,   1.04,  -4.45>, < -2.23,   0.05,  -4.45>, Rbond texture{pigment {color rgb <0.09, 0.33, 0.53> transmit 0.0} finish{ase3}}}
cylinder {< -2.23,  -0.94,  -4.46>, < -2.23,   0.05,  -4.45>, Rbond texture{pigment {color rgb <1.00, 0.05, 0.05> transmit 0.0} finish{ase3}}}
cylinder {< -2.23,   1.04,  -4.45>, < -1.61,   1.01,  -3.72>, Rbond texture{pigment {color rgb <0.09, 0.33, 0.53> transmit 0.0} finish{ase3}}}
cylinder {< -1.00,   0.99,  -2.99>, < -1.61,   1.01,  -3.72>, Rbond texture{pigment {color rgb <1.00, 0.05, 0.05> transmit 0.0} finish{ase3}}}
cylinder {< -2.23,   1.04,  -4.45>, < -2.23,   2.00,  -4.45>, Rbond texture{pigment {color rgb <0.09, 0.33, 0.53> transmit 0.0} finish{ase3}}}
cylinder {< -2.23,   2.97,  -4.45>, < -2.23,   2.00,  -4.45>, Rbond texture{pigment {color rgb <1.00, 0.05, 0.05> transmit 0.0} finish{ase3}}}
cylinder {< -2.23,   1.05,  -1.53>, < -2.23,   0.06,  -1.53>, Rbond texture{pigment {color rgb <0.09, 0.33, 0.53> transmit 0.0} finish{ase3}}}
cylinder {< -2.23,  -0.94,  -1.53>, < -2.23,   0.06,  -1.53>, Rbond texture{pigment {color rgb <1.00, 0.05, 0.05> transmit 0.0} finish{ase3}}}
cylinder {< -2.23,   1.05,  -1.53>, < -1.61,   1.02,  -2.26>, Rbond texture{pigment {color rgb <0.09, 0.33, 0.53> transmit 0.0} finish{ase3}}}
cylinder {< -1.00,   0.99,  -2.99>, < -1.61,   1.02,  -2.26>, Rbond texture{pigment {color rgb <1.00, 0.05, 0.05> transmit 0.0} finish{ase3}}}
cylinder {< -2.23,   1.05,  -1.53>, < -1.61,   1.02,  -0.80>, Rbond texture{pigment {color rgb <0.09, 0.33, 0.53> transmit 0.0} finish{ase3}}}
cylinder {< -1.00,   0.99,  -0.07>, < -1.61,   1.02,  -0.80>, Rbond texture{pigment {color rgb <1.00, 0.05, 0.05> transmit 0.0} finish{ase3}}}
cylinder {< -2.23,   1.05,  -1.53>, < -2.23,   2.01,  -1.53>, Rbond texture{pigment {color rgb <0.09, 0.33, 0.53> transmit 0.0} finish{ase3}}}
cylinder {< -2.23,   2.97,  -1.53>, < -2.23,   2.01,  -1.53>, Rbond texture{pigment {color rgb <1.00, 0.05, 0.05> transmit 0.0} finish{ase3}}}
cylinder {<  0.93,   0.96,  -2.96>, <  0.93,   0.36,  -3.71>, Rbond texture{pigment {color rgb <0.09, 0.33, 0.53> transmit 0.0} finish{ase3}}}
cylinder {<  0.93,  -0.23,  -4.45>, <  0.93,   0.36,  -3.71>, Rbond texture{pigment {color rgb <1.00, 0.05, 0.05> transmit 0.0} finish{ase3}}}
cylinder {<  0.93,   0.96,  -2.96>, <  0.93,   0.35,  -2.25>, Rbond texture{pigment {color rgb <0.09, 0.33, 0.53> transmit 0.0} finish{ase3}}}
cylinder {<  0.93,  -0.26,  -1.53>, <  0.93,   0.35,  -2.25>, Rbond texture{pigment {color rgb <1.00, 0.05, 0.05> transmit 0.0} finish{ase3}}}
cylinder {<  0.93,   0.96,  -2.96>, < -0.03,   0.97,  -2.98>, Rbond texture{pigment {color rgb <0.09, 0.33, 0.53> transmit 0.0} finish{ase3}}}
cylinder {< -1.00,   0.99,  -2.99>, < -0.03,   0.97,  -2.98>, Rbond texture{pigment {color rgb <1.00, 0.05, 0.05> transmit 0.0} finish{ase3}}}
cylinder {<  0.93,   0.96,  -2.96>, <  1.89,   0.97,  -2.98>, Rbond texture{pigment {color rgb <0.09, 0.33, 0.53> transmit 0.0} finish{ase3}}}
cylinder {<  2.86,   0.99,  -2.99>, <  1.89,   0.97,  -2.98>, Rbond texture{pigment {color rgb <1.00, 0.05, 0.05> transmit 0.0} finish{ase3}}}
cylinder {<  0.93,   0.96,  -2.96>, <  0.93,   1.56,  -3.71>, Rbond texture{pigment {color rgb <0.09, 0.33, 0.53> transmit 0.0} finish{ase3}}}
cylinder {<  0.93,   2.17,  -4.45>, <  0.93,   1.56,  -3.71>, Rbond texture{pigment {color rgb <1.00, 0.05, 0.05> transmit 0.0} finish{ase3}}}
cylinder {<  0.93,   0.96,  -2.96>, <  0.93,   1.58,  -2.25>, Rbond texture{pigment {color rgb <0.09, 0.33, 0.53> transmit 0.0} finish{ase3}}}
cylinder {<  0.93,   2.20,  -1.53>, <  0.93,   1.58,  -2.25>, Rbond texture{pigment {color rgb <1.00, 0.05, 0.05> transmit 0.0} finish{ase3}}}
cylinder {<  0.93,   0.96,  -0.10>, <  0.93,   0.35,  -0.81>, Rbond texture{pigment {color rgb <0.09, 0.33, 0.53> transmit 0.0} finish{ase3}}}
cylinder {<  0.93,  -0.26,  -1.53>, <  0.93,   0.35,  -0.81>, Rbond texture{pigment {color rgb <1.00, 0.05, 0.05> transmit 0.0} finish{ase3}}}
cylinder {<  0.93,   0.96,  -0.10>, < -0.03,   0.98,  -0.08>, Rbond texture{pigment {color rgb <0.09, 0.33, 0.53> transmit 0.0} finish{ase3}}}
cylinder {< -1.00,   0.99,  -0.07>, < -0.03,   0.98,  -0.08>, Rbond texture{pigment {color rgb <1.00, 0.05, 0.05> transmit 0.0} finish{ase3}}}
cylinder {<  0.93,   0.96,  -0.10>, <  1.89,   0.98,  -0.08>, Rbond texture{pigment {color rgb <0.09, 0.33, 0.53> transmit 0.0} finish{ase3}}}
cylinder {<  2.86,   1.00,  -0.07>, <  1.89,   0.98,  -0.08>, Rbond texture{pigment {color rgb <1.00, 0.05, 0.05> transmit 0.0} finish{ase3}}}
cylinder {<  0.93,   0.96,  -0.10>, <  0.93,   1.58,  -0.81>, Rbond texture{pigment {color rgb <0.09, 0.33, 0.53> transmit 0.0} finish{ase3}}}
cylinder {<  0.93,   2.20,  -1.53>, <  0.93,   1.58,  -0.81>, Rbond texture{pigment {color rgb <1.00, 0.05, 0.05> transmit 0.0} finish{ase3}}}
cylinder {< -2.23,   4.32,  -2.99>, < -2.23,   3.64,  -3.72>, Rbond texture{pigment {color rgb <0.09, 0.33, 0.53> transmit 0.0} finish{ase3}}}
cylinder {< -2.23,   2.97,  -4.45>, < -2.23,   3.64,  -3.72>, Rbond texture{pigment {color rgb <1.00, 0.05, 0.05> transmit 0.0} finish{ase3}}}
cylinder {< -2.23,   4.32,  -2.99>, < -2.23,   3.64,  -2.26>, Rbond texture{pigment {color rgb <0.09, 0.33, 0.53> transmit 0.0} finish{ase3}}}
cylinder {< -2.23,   2.97,  -1.53>, < -2.23,   3.64,  -2.26>, Rbond texture{pigment {color rgb <1.00, 0.05, 0.05> transmit 0.0} finish{ase3}}}
cylinder {< -2.23,   4.32,  -2.99>, < -1.24,   4.32,  -3.02>, Rbond texture{pigment {color rgb <0.09, 0.33, 0.53> transmit 0.0} finish{ase3}}}
cylinder {< -0.26,   4.32,  -3.06>, < -1.24,   4.32,  -3.02>, Rbond texture{pigment {color rgb <1.00, 0.05, 0.05> transmit 0.0} finish{ase3}}}
cylinder {< -2.23,   4.32,  -2.99>, < -2.23,   4.89,  -3.72>, Rbond texture{pigment {color rgb <0.09, 0.33, 0.53> transmit 0.0} finish{ase3}}}
cylinder {< -2.23,   5.46,  -4.45>, < -2.23,   4.89,  -3.72>, Rbond texture{pigment {color rgb <1.00, 0.05, 0.05> transmit 0.0} finish{ase3}}}
cylinder {< -2.23,   4.32,  -2.99>, < -2.23,   4.88,  -2.26>, Rbond texture{pigment {color rgb <0.09, 0.33, 0.53> transmit 0.0} finish{ase3}}}
cylinder {< -2.23,   5.44,  -1.52>, < -2.23,   4.88,  -2.26>, Rbond texture{pigment {color rgb <1.00, 0.05, 0.05> transmit 0.0} finish{ase3}}}
cylinder {< -2.23,   4.31,  -0.07>, < -2.23,   3.64,  -0.80>, Rbond texture{pigment {color rgb <0.09, 0.33, 0.53> transmit 0.0} finish{ase3}}}
cylinder {< -2.23,   2.97,  -1.53>, < -2.23,   3.64,  -0.80>, Rbond texture{pigment {color rgb <1.00, 0.05, 0.05> transmit 0.0} finish{ase3}}}
cylinder {< -2.23,   4.31,  -0.07>, < -1.25,   4.31,  -0.03>, Rbond texture{pigment {color rgb <0.09, 0.33, 0.53> transmit 0.0} finish{ase3}}}
cylinder {< -0.26,   4.32,  -0.00>, < -1.25,   4.31,  -0.03>, Rbond texture{pigment {color rgb <1.00, 0.05, 0.05> transmit 0.0} finish{ase3}}}
cylinder {< -2.23,   4.31,  -0.07>, < -2.23,   4.87,  -0.80>, Rbond texture{pigment {color rgb <0.09, 0.33, 0.53> transmit 0.0} finish{ase3}}}
cylinder {< -2.23,   5.44,  -1.52>, < -2.23,   4.87,  -0.80>, Rbond texture{pigment {color rgb <1.00, 0.05, 0.05> transmit 0.0} finish{ase3}}}
cylinder {<  0.93,   3.97,  -4.45>, <  0.93,   3.07,  -4.45>, Rbond texture{pigment {color rgb <0.09, 0.33, 0.53> transmit 0.0} finish{ase3}}}
cylinder {<  0.93,   2.17,  -4.45>, <  0.93,   3.07,  -4.45>, Rbond texture{pigment {color rgb <1.00, 0.05, 0.05> transmit 0.0} finish{ase3}}}
cylinder {<  0.93,   3.97,  -4.45>, <  0.33,   4.14,  -3.76>, Rbond texture{pigment {color rgb <0.09, 0.33, 0.53> transmit 0.0} finish{ase3}}}
cylinder {< -0.26,   4.32,  -3.06>, <  0.33,   4.14,  -3.76>, Rbond texture{pigment {color rgb <1.00, 0.05, 0.05> transmit 0.0} finish{ase3}}}
cylinder {<  0.93,   3.97,  -4.45>, <  1.53,   4.14,  -3.76>, Rbond texture{pigment {color rgb <0.09, 0.33, 0.53> transmit 0.0} finish{ase3}}}
cylinder {<  2.13,   4.32,  -3.06>, <  1.53,   4.14,  -3.76>, Rbond texture{pigment {color rgb <1.00, 0.05, 0.05> transmit 0.0} finish{ase3}}}
cylinder {<  0.93,   4.41,  -1.53>, <  0.93,   5.44,  -1.53>, Rbond texture{pigment {color rgb <0.40, 0.56, 0.56> transmit 0.0} finish{ase3}}}
cylinder {<  0.93,   6.46,  -1.54>, <  0.93,   5.44,  -1.53>, Rbond texture{pigment {color rgb <0.56, 0.56, 0.56> transmit 0.0} finish{ase3}}}
cylinder {<  0.93,   4.41,  -1.53>, <  0.93,   3.31,  -1.53>, Rbond texture{pigment {color rgb <0.40, 0.56, 0.56> transmit 0.0} finish{ase3}}}
cylinder {<  0.93,   2.20,  -1.53>, <  0.93,   3.31,  -1.53>, Rbond texture{pigment {color rgb <1.00, 0.05, 0.05> transmit 0.0} finish{ase3}}}
cylinder {<  0.93,   4.41,  -1.53>, <  0.34,   4.37,  -2.29>, Rbond texture{pigment {color rgb <0.40, 0.56, 0.56> transmit 0.0} finish{ase3}}}
cylinder {< -0.26,   4.32,  -3.06>, <  0.34,   4.37,  -2.29>, Rbond texture{pigment {color rgb <1.00, 0.05, 0.05> transmit 0.0} finish{ase3}}}
cylinder {<  0.93,   4.41,  -1.53>, <  0.34,   4.36,  -0.77>, Rbond texture{pigment {color rgb <0.40, 0.56, 0.56> transmit 0.0} finish{ase3}}}
cylinder {< -0.26,   4.32,  -0.00>, <  0.34,   4.36,  -0.77>, Rbond texture{pigment {color rgb <1.00, 0.05, 0.05> transmit 0.0} finish{ase3}}}
cylinder {<  0.93,   4.41,  -1.53>, <  1.53,   4.37,  -2.29>, Rbond texture{pigment {color rgb <0.40, 0.56, 0.56> transmit 0.0} finish{ase3}}}
cylinder {<  2.13,   4.32,  -3.06>, <  1.53,   4.37,  -2.29>, Rbond texture{pigment {color rgb <1.00, 0.05, 0.05> transmit 0.0} finish{ase3}}}
cylinder {<  0.93,   4.41,  -1.53>, <  1.53,   4.36,  -0.77>, Rbond texture{pigment {color rgb <0.40, 0.56, 0.56> transmit 0.0} finish{ase3}}}
cylinder {<  2.13,   4.32,   0.00>, <  1.53,   4.36,  -0.77>, Rbond texture{pigment {color rgb <1.00, 0.05, 0.05> transmit 0.0} finish{ase3}}}
