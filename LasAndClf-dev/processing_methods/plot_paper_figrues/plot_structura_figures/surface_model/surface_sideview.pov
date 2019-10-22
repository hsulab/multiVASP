#include "colors.inc"
#include "finish.inc"

global_settings {assumed_gamma 1 max_trace_level 6}
background {color White}
camera {perspective
  right -7.20*x up 13.78*y
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

atom(<  0.93,  -6.00,  -4.38>, 0.56, rgb <1.00, 0.05, 0.05>, 0.0, ase3) // #0 
atom(<  0.93,  -6.00,  -1.46>, 0.56, rgb <1.00, 0.05, 0.05>, 0.0, ase3) // #1 
atom(< -1.00,  -4.78,  -2.92>, 0.56, rgb <1.00, 0.05, 0.05>, 0.0, ase3) // #2 
atom(< -1.00,  -4.78,   0.00>, 0.56, rgb <1.00, 0.05, 0.05>, 0.0, ase3) // #3 
atom(<  2.87,  -4.78,  -2.92>, 0.56, rgb <1.00, 0.05, 0.05>, 0.0, ase3) // #4 
atom(<  2.87,  -4.78,   0.00>, 0.56, rgb <1.00, 0.05, 0.05>, 0.0, ase3) // #5 
atom(<  0.93,  -3.55,  -4.38>, 0.56, rgb <1.00, 0.05, 0.05>, 0.0, ase3) // #6 
atom(<  0.93,  -3.55,  -1.46>, 0.56, rgb <1.00, 0.05, 0.05>, 0.0, ase3) // #7 
atom(< -2.23,  -2.84,  -4.38>, 0.56, rgb <1.00, 0.05, 0.05>, 0.0, ase3) // #8 
atom(< -2.23,  -2.84,  -1.46>, 0.56, rgb <1.00, 0.05, 0.05>, 0.0, ase3) // #9 
atom(< -0.29,  -1.62,  -2.92>, 0.56, rgb <1.00, 0.05, 0.05>, 0.0, ase3) // #10 
atom(< -0.29,  -1.62,   0.00>, 0.56, rgb <1.00, 0.05, 0.05>, 0.0, ase3) // #11 
atom(<  2.16,  -1.62,  -2.92>, 0.56, rgb <1.00, 0.05, 0.05>, 0.0, ase3) // #12 
atom(<  2.16,  -1.62,   0.00>, 0.56, rgb <1.00, 0.05, 0.05>, 0.0, ase3) // #13 
atom(< -2.23,  -0.39,  -4.38>, 0.56, rgb <1.00, 0.05, 0.05>, 0.0, ase3) // #14 
atom(< -2.23,  -0.39,  -1.46>, 0.56, rgb <1.00, 0.05, 0.05>, 0.0, ase3) // #15 
atom(<  0.93,   0.30,  -4.38>, 0.56, rgb <1.00, 0.05, 0.05>, 0.0, ase3) // #16 
atom(<  0.93,   0.30,  -1.46>, 0.56, rgb <1.00, 0.05, 0.05>, 0.0, ase3) // #17 
atom(< -0.99,   1.54,  -2.92>, 0.56, rgb <1.00, 0.05, 0.05>, 0.0, ase3) // #18 
atom(< -0.99,   1.54,  -0.00>, 0.56, rgb <1.00, 0.05, 0.05>, 0.0, ase3) // #19 
atom(<  2.85,   1.54,  -2.92>, 0.56, rgb <1.00, 0.05, 0.05>, 0.0, ase3) // #20 
atom(<  2.85,   1.54,  -0.00>, 0.56, rgb <1.00, 0.05, 0.05>, 0.0, ase3) // #21 
atom(<  0.93,   2.74,  -4.38>, 0.56, rgb <1.00, 0.05, 0.05>, 0.0, ase3) // #22 
atom(<  0.93,   2.74,  -1.46>, 0.56, rgb <1.00, 0.05, 0.05>, 0.0, ase3) // #23 
atom(< -2.23,   3.51,  -4.38>, 0.56, rgb <1.00, 0.05, 0.05>, 0.0, ase3) // #24 
atom(< -2.23,   3.51,  -1.46>, 0.56, rgb <1.00, 0.05, 0.05>, 0.0, ase3) // #25 
atom(< -0.24,   4.87,  -2.92>, 0.56, rgb <1.00, 0.05, 0.05>, 0.0, ase3) // #26 
atom(< -0.24,   4.87,  -0.00>, 0.56, rgb <1.00, 0.05, 0.05>, 0.0, ase3) // #27 
atom(<  2.11,   4.87,  -2.92>, 0.56, rgb <1.00, 0.05, 0.05>, 0.0, ase3) // #28 
atom(<  2.11,   4.87,  -0.00>, 0.56, rgb <1.00, 0.05, 0.05>, 0.0, ase3) // #29 
atom(< -2.23,   6.00,  -4.38>, 0.56, rgb <1.00, 0.05, 0.05>, 0.0, ase3) // #30 
atom(< -2.23,   6.00,  -1.46>, 0.56, rgb <1.00, 0.05, 0.05>, 0.0, ase3) // #31 
atom(< -2.23,  -4.78,  -4.38>, 1.20, rgb <0.09, 0.33, 0.53>, 0.0, ase3) // #32 
atom(< -2.23,  -4.78,  -1.46>, 1.20, rgb <0.09, 0.33, 0.53>, 0.0, ase3) // #33 
atom(<  0.93,  -4.78,  -2.92>, 1.20, rgb <0.09, 0.33, 0.53>, 0.0, ase3) // #34 
atom(<  0.93,  -4.78,   0.00>, 1.20, rgb <0.09, 0.33, 0.53>, 0.0, ase3) // #35 
atom(< -2.23,  -1.62,  -2.92>, 1.20, rgb <0.09, 0.33, 0.53>, 0.0, ase3) // #36 
atom(< -2.23,  -1.62,   0.00>, 1.20, rgb <0.09, 0.33, 0.53>, 0.0, ase3) // #37 
atom(<  0.93,  -1.62,  -4.38>, 1.20, rgb <0.09, 0.33, 0.53>, 0.0, ase3) // #38 
atom(<  0.93,  -1.62,  -1.46>, 1.20, rgb <0.09, 0.33, 0.53>, 0.0, ase3) // #39 
atom(< -2.23,   1.61,  -4.38>, 1.20, rgb <0.09, 0.33, 0.53>, 0.0, ase3) // #40 
atom(< -2.23,   1.61,  -1.46>, 1.20, rgb <0.09, 0.33, 0.53>, 0.0, ase3) // #41 
atom(<  0.93,   1.48,  -2.92>, 1.20, rgb <0.09, 0.33, 0.53>, 0.0, ase3) // #42 
atom(<  0.93,   1.48,  -0.00>, 1.20, rgb <0.09, 0.33, 0.53>, 0.0, ase3) // #43 
atom(< -2.23,   4.90,  -2.92>, 1.20, rgb <0.09, 0.33, 0.53>, 0.0, ase3) // #44 
atom(< -2.23,   4.90,  -0.00>, 1.20, rgb <0.09, 0.33, 0.53>, 0.0, ase3) // #45 
atom(<  0.93,   4.57,  -4.38>, 1.20, rgb <0.09, 0.33, 0.53>, 0.0, ase3) // #46 
atom(<  0.93,   4.57,  -1.46>, 1.02, rgb <0.40, 0.56, 0.56>, 0.0, ase3) // #47 
cylinder {< -2.23,  -4.78,  -4.38>, < -1.62,  -4.78,  -3.65>, Rbond texture{pigment {color rgb <0.09, 0.33, 0.53> transmit 0.0} finish{ase3}}}
cylinder {< -1.00,  -4.78,  -2.92>, < -1.62,  -4.78,  -3.65>, Rbond texture{pigment {color rgb <1.00, 0.05, 0.05> transmit 0.0} finish{ase3}}}
cylinder {< -2.23,  -4.78,  -4.38>, < -2.23,  -3.81,  -4.38>, Rbond texture{pigment {color rgb <0.09, 0.33, 0.53> transmit 0.0} finish{ase3}}}
cylinder {< -2.23,  -2.84,  -4.38>, < -2.23,  -3.81,  -4.38>, Rbond texture{pigment {color rgb <1.00, 0.05, 0.05> transmit 0.0} finish{ase3}}}
cylinder {< -2.23,  -4.78,  -1.46>, < -1.62,  -4.78,  -2.19>, Rbond texture{pigment {color rgb <0.09, 0.33, 0.53> transmit 0.0} finish{ase3}}}
cylinder {< -1.00,  -4.78,  -2.92>, < -1.62,  -4.78,  -2.19>, Rbond texture{pigment {color rgb <1.00, 0.05, 0.05> transmit 0.0} finish{ase3}}}
cylinder {< -2.23,  -4.78,  -1.46>, < -1.62,  -4.78,  -0.73>, Rbond texture{pigment {color rgb <0.09, 0.33, 0.53> transmit 0.0} finish{ase3}}}
cylinder {< -1.00,  -4.78,   0.00>, < -1.62,  -4.78,  -0.73>, Rbond texture{pigment {color rgb <1.00, 0.05, 0.05> transmit 0.0} finish{ase3}}}
cylinder {< -2.23,  -4.78,  -1.46>, < -2.23,  -3.81,  -1.46>, Rbond texture{pigment {color rgb <0.09, 0.33, 0.53> transmit 0.0} finish{ase3}}}
cylinder {< -2.23,  -2.84,  -1.46>, < -2.23,  -3.81,  -1.46>, Rbond texture{pigment {color rgb <1.00, 0.05, 0.05> transmit 0.0} finish{ase3}}}
cylinder {<  0.93,  -4.78,  -2.92>, <  0.93,  -5.39,  -3.65>, Rbond texture{pigment {color rgb <0.09, 0.33, 0.53> transmit 0.0} finish{ase3}}}
cylinder {<  0.93,  -6.00,  -4.38>, <  0.93,  -5.39,  -3.65>, Rbond texture{pigment {color rgb <1.00, 0.05, 0.05> transmit 0.0} finish{ase3}}}
cylinder {<  0.93,  -4.78,  -2.92>, <  0.93,  -5.39,  -2.19>, Rbond texture{pigment {color rgb <0.09, 0.33, 0.53> transmit 0.0} finish{ase3}}}
cylinder {<  0.93,  -6.00,  -1.46>, <  0.93,  -5.39,  -2.19>, Rbond texture{pigment {color rgb <1.00, 0.05, 0.05> transmit 0.0} finish{ase3}}}
cylinder {<  0.93,  -4.78,  -2.92>, < -0.04,  -4.78,  -2.92>, Rbond texture{pigment {color rgb <0.09, 0.33, 0.53> transmit 0.0} finish{ase3}}}
cylinder {< -1.00,  -4.78,  -2.92>, < -0.04,  -4.78,  -2.92>, Rbond texture{pigment {color rgb <1.00, 0.05, 0.05> transmit 0.0} finish{ase3}}}
cylinder {<  0.93,  -4.78,  -2.92>, <  1.90,  -4.78,  -2.92>, Rbond texture{pigment {color rgb <0.09, 0.33, 0.53> transmit 0.0} finish{ase3}}}
cylinder {<  2.87,  -4.78,  -2.92>, <  1.90,  -4.78,  -2.92>, Rbond texture{pigment {color rgb <1.00, 0.05, 0.05> transmit 0.0} finish{ase3}}}
cylinder {<  0.93,  -4.78,  -2.92>, <  0.93,  -4.16,  -3.65>, Rbond texture{pigment {color rgb <0.09, 0.33, 0.53> transmit 0.0} finish{ase3}}}
cylinder {<  0.93,  -3.55,  -4.38>, <  0.93,  -4.16,  -3.65>, Rbond texture{pigment {color rgb <1.00, 0.05, 0.05> transmit 0.0} finish{ase3}}}
cylinder {<  0.93,  -4.78,  -2.92>, <  0.93,  -4.16,  -2.19>, Rbond texture{pigment {color rgb <0.09, 0.33, 0.53> transmit 0.0} finish{ase3}}}
cylinder {<  0.93,  -3.55,  -1.46>, <  0.93,  -4.16,  -2.19>, Rbond texture{pigment {color rgb <1.00, 0.05, 0.05> transmit 0.0} finish{ase3}}}
cylinder {<  0.93,  -4.78,   0.00>, <  0.93,  -5.39,  -0.73>, Rbond texture{pigment {color rgb <0.09, 0.33, 0.53> transmit 0.0} finish{ase3}}}
cylinder {<  0.93,  -6.00,  -1.46>, <  0.93,  -5.39,  -0.73>, Rbond texture{pigment {color rgb <1.00, 0.05, 0.05> transmit 0.0} finish{ase3}}}
cylinder {<  0.93,  -4.78,   0.00>, < -0.04,  -4.78,   0.00>, Rbond texture{pigment {color rgb <0.09, 0.33, 0.53> transmit 0.0} finish{ase3}}}
cylinder {< -1.00,  -4.78,   0.00>, < -0.04,  -4.78,   0.00>, Rbond texture{pigment {color rgb <1.00, 0.05, 0.05> transmit 0.0} finish{ase3}}}
cylinder {<  0.93,  -4.78,   0.00>, <  1.90,  -4.78,   0.00>, Rbond texture{pigment {color rgb <0.09, 0.33, 0.53> transmit 0.0} finish{ase3}}}
cylinder {<  2.87,  -4.78,   0.00>, <  1.90,  -4.78,   0.00>, Rbond texture{pigment {color rgb <1.00, 0.05, 0.05> transmit 0.0} finish{ase3}}}
cylinder {<  0.93,  -4.78,   0.00>, <  0.93,  -4.16,  -0.73>, Rbond texture{pigment {color rgb <0.09, 0.33, 0.53> transmit 0.0} finish{ase3}}}
cylinder {<  0.93,  -3.55,  -1.46>, <  0.93,  -4.16,  -0.73>, Rbond texture{pigment {color rgb <1.00, 0.05, 0.05> transmit 0.0} finish{ase3}}}
cylinder {< -2.23,  -1.62,  -2.92>, < -2.23,  -2.23,  -3.65>, Rbond texture{pigment {color rgb <0.09, 0.33, 0.53> transmit 0.0} finish{ase3}}}
cylinder {< -2.23,  -2.84,  -4.38>, < -2.23,  -2.23,  -3.65>, Rbond texture{pigment {color rgb <1.00, 0.05, 0.05> transmit 0.0} finish{ase3}}}
cylinder {< -2.23,  -1.62,  -2.92>, < -2.23,  -2.23,  -2.19>, Rbond texture{pigment {color rgb <0.09, 0.33, 0.53> transmit 0.0} finish{ase3}}}
cylinder {< -2.23,  -2.84,  -1.46>, < -2.23,  -2.23,  -2.19>, Rbond texture{pigment {color rgb <1.00, 0.05, 0.05> transmit 0.0} finish{ase3}}}
cylinder {< -2.23,  -1.62,  -2.92>, < -1.26,  -1.62,  -2.92>, Rbond texture{pigment {color rgb <0.09, 0.33, 0.53> transmit 0.0} finish{ase3}}}
cylinder {< -0.29,  -1.62,  -2.92>, < -1.26,  -1.62,  -2.92>, Rbond texture{pigment {color rgb <1.00, 0.05, 0.05> transmit 0.0} finish{ase3}}}
cylinder {< -2.23,  -1.62,  -2.92>, < -2.23,  -1.01,  -3.65>, Rbond texture{pigment {color rgb <0.09, 0.33, 0.53> transmit 0.0} finish{ase3}}}
cylinder {< -2.23,  -0.39,  -4.38>, < -2.23,  -1.01,  -3.65>, Rbond texture{pigment {color rgb <1.00, 0.05, 0.05> transmit 0.0} finish{ase3}}}
cylinder {< -2.23,  -1.62,  -2.92>, < -2.23,  -1.01,  -2.19>, Rbond texture{pigment {color rgb <0.09, 0.33, 0.53> transmit 0.0} finish{ase3}}}
cylinder {< -2.23,  -0.39,  -1.46>, < -2.23,  -1.01,  -2.19>, Rbond texture{pigment {color rgb <1.00, 0.05, 0.05> transmit 0.0} finish{ase3}}}
cylinder {< -2.23,  -1.62,   0.00>, < -2.23,  -2.23,  -0.73>, Rbond texture{pigment {color rgb <0.09, 0.33, 0.53> transmit 0.0} finish{ase3}}}
cylinder {< -2.23,  -2.84,  -1.46>, < -2.23,  -2.23,  -0.73>, Rbond texture{pigment {color rgb <1.00, 0.05, 0.05> transmit 0.0} finish{ase3}}}
cylinder {< -2.23,  -1.62,   0.00>, < -1.26,  -1.62,   0.00>, Rbond texture{pigment {color rgb <0.09, 0.33, 0.53> transmit 0.0} finish{ase3}}}
cylinder {< -0.29,  -1.62,   0.00>, < -1.26,  -1.62,   0.00>, Rbond texture{pigment {color rgb <1.00, 0.05, 0.05> transmit 0.0} finish{ase3}}}
cylinder {< -2.23,  -1.62,   0.00>, < -2.23,  -1.01,  -0.73>, Rbond texture{pigment {color rgb <0.09, 0.33, 0.53> transmit 0.0} finish{ase3}}}
cylinder {< -2.23,  -0.39,  -1.46>, < -2.23,  -1.01,  -0.73>, Rbond texture{pigment {color rgb <1.00, 0.05, 0.05> transmit 0.0} finish{ase3}}}
cylinder {<  0.93,  -1.62,  -4.38>, <  0.93,  -2.58,  -4.38>, Rbond texture{pigment {color rgb <0.09, 0.33, 0.53> transmit 0.0} finish{ase3}}}
cylinder {<  0.93,  -3.55,  -4.38>, <  0.93,  -2.58,  -4.38>, Rbond texture{pigment {color rgb <1.00, 0.05, 0.05> transmit 0.0} finish{ase3}}}
cylinder {<  0.93,  -1.62,  -4.38>, <  0.32,  -1.62,  -3.65>, Rbond texture{pigment {color rgb <0.09, 0.33, 0.53> transmit 0.0} finish{ase3}}}
cylinder {< -0.29,  -1.62,  -2.92>, <  0.32,  -1.62,  -3.65>, Rbond texture{pigment {color rgb <1.00, 0.05, 0.05> transmit 0.0} finish{ase3}}}
cylinder {<  0.93,  -1.62,  -4.38>, <  1.54,  -1.62,  -3.65>, Rbond texture{pigment {color rgb <0.09, 0.33, 0.53> transmit 0.0} finish{ase3}}}
cylinder {<  2.16,  -1.62,  -2.92>, <  1.54,  -1.62,  -3.65>, Rbond texture{pigment {color rgb <1.00, 0.05, 0.05> transmit 0.0} finish{ase3}}}
cylinder {<  0.93,  -1.62,  -4.38>, <  0.93,  -0.66,  -4.38>, Rbond texture{pigment {color rgb <0.09, 0.33, 0.53> transmit 0.0} finish{ase3}}}
cylinder {<  0.93,   0.30,  -4.38>, <  0.93,  -0.66,  -4.38>, Rbond texture{pigment {color rgb <1.00, 0.05, 0.05> transmit 0.0} finish{ase3}}}
cylinder {<  0.93,  -1.62,  -1.46>, <  0.93,  -2.58,  -1.46>, Rbond texture{pigment {color rgb <0.09, 0.33, 0.53> transmit 0.0} finish{ase3}}}
cylinder {<  0.93,  -3.55,  -1.46>, <  0.93,  -2.58,  -1.46>, Rbond texture{pigment {color rgb <1.00, 0.05, 0.05> transmit 0.0} finish{ase3}}}
cylinder {<  0.93,  -1.62,  -1.46>, <  0.32,  -1.62,  -2.19>, Rbond texture{pigment {color rgb <0.09, 0.33, 0.53> transmit 0.0} finish{ase3}}}
cylinder {< -0.29,  -1.62,  -2.92>, <  0.32,  -1.62,  -2.19>, Rbond texture{pigment {color rgb <1.00, 0.05, 0.05> transmit 0.0} finish{ase3}}}
cylinder {<  0.93,  -1.62,  -1.46>, <  0.32,  -1.62,  -0.73>, Rbond texture{pigment {color rgb <0.09, 0.33, 0.53> transmit 0.0} finish{ase3}}}
cylinder {< -0.29,  -1.62,   0.00>, <  0.32,  -1.62,  -0.73>, Rbond texture{pigment {color rgb <1.00, 0.05, 0.05> transmit 0.0} finish{ase3}}}
cylinder {<  0.93,  -1.62,  -1.46>, <  1.54,  -1.62,  -2.19>, Rbond texture{pigment {color rgb <0.09, 0.33, 0.53> transmit 0.0} finish{ase3}}}
cylinder {<  2.16,  -1.62,  -2.92>, <  1.54,  -1.62,  -2.19>, Rbond texture{pigment {color rgb <1.00, 0.05, 0.05> transmit 0.0} finish{ase3}}}
cylinder {<  0.93,  -1.62,  -1.46>, <  1.54,  -1.62,  -0.73>, Rbond texture{pigment {color rgb <0.09, 0.33, 0.53> transmit 0.0} finish{ase3}}}
cylinder {<  2.16,  -1.62,   0.00>, <  1.54,  -1.62,  -0.73>, Rbond texture{pigment {color rgb <1.00, 0.05, 0.05> transmit 0.0} finish{ase3}}}
cylinder {<  0.93,  -1.62,  -1.46>, <  0.93,  -0.66,  -1.46>, Rbond texture{pigment {color rgb <0.09, 0.33, 0.53> transmit 0.0} finish{ase3}}}
cylinder {<  0.93,   0.30,  -1.46>, <  0.93,  -0.66,  -1.46>, Rbond texture{pigment {color rgb <1.00, 0.05, 0.05> transmit 0.0} finish{ase3}}}
cylinder {< -2.23,   1.61,  -4.38>, < -2.23,   0.61,  -4.38>, Rbond texture{pigment {color rgb <0.09, 0.33, 0.53> transmit 0.0} finish{ase3}}}
cylinder {< -2.23,  -0.39,  -4.38>, < -2.23,   0.61,  -4.38>, Rbond texture{pigment {color rgb <1.00, 0.05, 0.05> transmit 0.0} finish{ase3}}}
cylinder {< -2.23,   1.61,  -4.38>, < -1.61,   1.57,  -3.65>, Rbond texture{pigment {color rgb <0.09, 0.33, 0.53> transmit 0.0} finish{ase3}}}
cylinder {< -0.99,   1.54,  -2.92>, < -1.61,   1.57,  -3.65>, Rbond texture{pigment {color rgb <1.00, 0.05, 0.05> transmit 0.0} finish{ase3}}}
cylinder {< -2.23,   1.61,  -4.38>, < -2.23,   2.56,  -4.38>, Rbond texture{pigment {color rgb <0.09, 0.33, 0.53> transmit 0.0} finish{ase3}}}
cylinder {< -2.23,   3.51,  -4.38>, < -2.23,   2.56,  -4.38>, Rbond texture{pigment {color rgb <1.00, 0.05, 0.05> transmit 0.0} finish{ase3}}}
cylinder {< -2.23,   1.61,  -1.46>, < -2.23,   0.61,  -1.46>, Rbond texture{pigment {color rgb <0.09, 0.33, 0.53> transmit 0.0} finish{ase3}}}
cylinder {< -2.23,  -0.39,  -1.46>, < -2.23,   0.61,  -1.46>, Rbond texture{pigment {color rgb <1.00, 0.05, 0.05> transmit 0.0} finish{ase3}}}
cylinder {< -2.23,   1.61,  -1.46>, < -1.61,   1.57,  -2.19>, Rbond texture{pigment {color rgb <0.09, 0.33, 0.53> transmit 0.0} finish{ase3}}}
cylinder {< -0.99,   1.54,  -2.92>, < -1.61,   1.57,  -2.19>, Rbond texture{pigment {color rgb <1.00, 0.05, 0.05> transmit 0.0} finish{ase3}}}
cylinder {< -2.23,   1.61,  -1.46>, < -1.61,   1.57,  -0.73>, Rbond texture{pigment {color rgb <0.09, 0.33, 0.53> transmit 0.0} finish{ase3}}}
cylinder {< -0.99,   1.54,  -0.00>, < -1.61,   1.57,  -0.73>, Rbond texture{pigment {color rgb <1.00, 0.05, 0.05> transmit 0.0} finish{ase3}}}
cylinder {< -2.23,   1.61,  -1.46>, < -2.23,   2.56,  -1.46>, Rbond texture{pigment {color rgb <0.09, 0.33, 0.53> transmit 0.0} finish{ase3}}}
cylinder {< -2.23,   3.51,  -1.46>, < -2.23,   2.56,  -1.46>, Rbond texture{pigment {color rgb <1.00, 0.05, 0.05> transmit 0.0} finish{ase3}}}
cylinder {<  0.93,   1.48,  -2.92>, <  0.93,   0.89,  -3.65>, Rbond texture{pigment {color rgb <0.09, 0.33, 0.53> transmit 0.0} finish{ase3}}}
cylinder {<  0.93,   0.30,  -4.38>, <  0.93,   0.89,  -3.65>, Rbond texture{pigment {color rgb <1.00, 0.05, 0.05> transmit 0.0} finish{ase3}}}
cylinder {<  0.93,   1.48,  -2.92>, <  0.93,   0.89,  -2.19>, Rbond texture{pigment {color rgb <0.09, 0.33, 0.53> transmit 0.0} finish{ase3}}}
cylinder {<  0.93,   0.30,  -1.46>, <  0.93,   0.89,  -2.19>, Rbond texture{pigment {color rgb <1.00, 0.05, 0.05> transmit 0.0} finish{ase3}}}
cylinder {<  0.93,   1.48,  -2.92>, < -0.03,   1.51,  -2.92>, Rbond texture{pigment {color rgb <0.09, 0.33, 0.53> transmit 0.0} finish{ase3}}}
cylinder {< -0.99,   1.54,  -2.92>, < -0.03,   1.51,  -2.92>, Rbond texture{pigment {color rgb <1.00, 0.05, 0.05> transmit 0.0} finish{ase3}}}
cylinder {<  0.93,   1.48,  -2.92>, <  1.89,   1.51,  -2.92>, Rbond texture{pigment {color rgb <0.09, 0.33, 0.53> transmit 0.0} finish{ase3}}}
cylinder {<  2.85,   1.54,  -2.92>, <  1.89,   1.51,  -2.92>, Rbond texture{pigment {color rgb <1.00, 0.05, 0.05> transmit 0.0} finish{ase3}}}
cylinder {<  0.93,   1.48,  -2.92>, <  0.93,   2.11,  -3.65>, Rbond texture{pigment {color rgb <0.09, 0.33, 0.53> transmit 0.0} finish{ase3}}}
cylinder {<  0.93,   2.74,  -4.38>, <  0.93,   2.11,  -3.65>, Rbond texture{pigment {color rgb <1.00, 0.05, 0.05> transmit 0.0} finish{ase3}}}
cylinder {<  0.93,   1.48,  -2.92>, <  0.93,   2.11,  -2.19>, Rbond texture{pigment {color rgb <0.09, 0.33, 0.53> transmit 0.0} finish{ase3}}}
cylinder {<  0.93,   2.74,  -1.46>, <  0.93,   2.11,  -2.19>, Rbond texture{pigment {color rgb <1.00, 0.05, 0.05> transmit 0.0} finish{ase3}}}
cylinder {<  0.93,   1.48,  -0.00>, <  0.93,   0.89,  -0.73>, Rbond texture{pigment {color rgb <0.09, 0.33, 0.53> transmit 0.0} finish{ase3}}}
cylinder {<  0.93,   0.30,  -1.46>, <  0.93,   0.89,  -0.73>, Rbond texture{pigment {color rgb <1.00, 0.05, 0.05> transmit 0.0} finish{ase3}}}
cylinder {<  0.93,   1.48,  -0.00>, < -0.03,   1.51,  -0.00>, Rbond texture{pigment {color rgb <0.09, 0.33, 0.53> transmit 0.0} finish{ase3}}}
cylinder {< -0.99,   1.54,  -0.00>, < -0.03,   1.51,  -0.00>, Rbond texture{pigment {color rgb <1.00, 0.05, 0.05> transmit 0.0} finish{ase3}}}
cylinder {<  0.93,   1.48,  -0.00>, <  1.89,   1.51,  -0.00>, Rbond texture{pigment {color rgb <0.09, 0.33, 0.53> transmit 0.0} finish{ase3}}}
cylinder {<  2.85,   1.54,  -0.00>, <  1.89,   1.51,  -0.00>, Rbond texture{pigment {color rgb <1.00, 0.05, 0.05> transmit 0.0} finish{ase3}}}
cylinder {<  0.93,   1.48,  -0.00>, <  0.93,   2.11,  -0.73>, Rbond texture{pigment {color rgb <0.09, 0.33, 0.53> transmit 0.0} finish{ase3}}}
cylinder {<  0.93,   2.74,  -1.46>, <  0.93,   2.11,  -0.73>, Rbond texture{pigment {color rgb <1.00, 0.05, 0.05> transmit 0.0} finish{ase3}}}
cylinder {< -2.23,   4.90,  -2.92>, < -2.23,   4.20,  -3.65>, Rbond texture{pigment {color rgb <0.09, 0.33, 0.53> transmit 0.0} finish{ase3}}}
cylinder {< -2.23,   3.51,  -4.38>, < -2.23,   4.20,  -3.65>, Rbond texture{pigment {color rgb <1.00, 0.05, 0.05> transmit 0.0} finish{ase3}}}
cylinder {< -2.23,   4.90,  -2.92>, < -2.23,   4.20,  -2.19>, Rbond texture{pigment {color rgb <0.09, 0.33, 0.53> transmit 0.0} finish{ase3}}}
cylinder {< -2.23,   3.51,  -1.46>, < -2.23,   4.20,  -2.19>, Rbond texture{pigment {color rgb <1.00, 0.05, 0.05> transmit 0.0} finish{ase3}}}
cylinder {< -2.23,   4.90,  -2.92>, < -1.23,   4.88,  -2.92>, Rbond texture{pigment {color rgb <0.09, 0.33, 0.53> transmit 0.0} finish{ase3}}}
cylinder {< -0.24,   4.87,  -2.92>, < -1.23,   4.88,  -2.92>, Rbond texture{pigment {color rgb <1.00, 0.05, 0.05> transmit 0.0} finish{ase3}}}
cylinder {< -2.23,   4.90,  -2.92>, < -2.23,   5.45,  -3.65>, Rbond texture{pigment {color rgb <0.09, 0.33, 0.53> transmit 0.0} finish{ase3}}}
cylinder {< -2.23,   6.00,  -4.38>, < -2.23,   5.45,  -3.65>, Rbond texture{pigment {color rgb <1.00, 0.05, 0.05> transmit 0.0} finish{ase3}}}
cylinder {< -2.23,   4.90,  -2.92>, < -2.23,   5.45,  -2.19>, Rbond texture{pigment {color rgb <0.09, 0.33, 0.53> transmit 0.0} finish{ase3}}}
cylinder {< -2.23,   6.00,  -1.46>, < -2.23,   5.45,  -2.19>, Rbond texture{pigment {color rgb <1.00, 0.05, 0.05> transmit 0.0} finish{ase3}}}
cylinder {< -2.23,   4.90,  -0.00>, < -2.23,   4.20,  -0.73>, Rbond texture{pigment {color rgb <0.09, 0.33, 0.53> transmit 0.0} finish{ase3}}}
cylinder {< -2.23,   3.51,  -1.46>, < -2.23,   4.20,  -0.73>, Rbond texture{pigment {color rgb <1.00, 0.05, 0.05> transmit 0.0} finish{ase3}}}
cylinder {< -2.23,   4.90,  -0.00>, < -1.23,   4.88,  -0.00>, Rbond texture{pigment {color rgb <0.09, 0.33, 0.53> transmit 0.0} finish{ase3}}}
cylinder {< -0.24,   4.87,  -0.00>, < -1.23,   4.88,  -0.00>, Rbond texture{pigment {color rgb <1.00, 0.05, 0.05> transmit 0.0} finish{ase3}}}
cylinder {< -2.23,   4.90,  -0.00>, < -2.23,   5.45,  -0.73>, Rbond texture{pigment {color rgb <0.09, 0.33, 0.53> transmit 0.0} finish{ase3}}}
cylinder {< -2.23,   6.00,  -1.46>, < -2.23,   5.45,  -0.73>, Rbond texture{pigment {color rgb <1.00, 0.05, 0.05> transmit 0.0} finish{ase3}}}
cylinder {<  0.93,   4.57,  -4.38>, <  0.93,   3.66,  -4.38>, Rbond texture{pigment {color rgb <0.09, 0.33, 0.53> transmit 0.0} finish{ase3}}}
cylinder {<  0.93,   2.74,  -4.38>, <  0.93,   3.66,  -4.38>, Rbond texture{pigment {color rgb <1.00, 0.05, 0.05> transmit 0.0} finish{ase3}}}
cylinder {<  0.93,   4.57,  -4.38>, <  0.35,   4.72,  -3.65>, Rbond texture{pigment {color rgb <0.09, 0.33, 0.53> transmit 0.0} finish{ase3}}}
cylinder {< -0.24,   4.87,  -2.92>, <  0.35,   4.72,  -3.65>, Rbond texture{pigment {color rgb <1.00, 0.05, 0.05> transmit 0.0} finish{ase3}}}
cylinder {<  0.93,   4.57,  -4.38>, <  1.52,   4.72,  -3.65>, Rbond texture{pigment {color rgb <0.09, 0.33, 0.53> transmit 0.0} finish{ase3}}}
cylinder {<  2.11,   4.87,  -2.92>, <  1.52,   4.72,  -3.65>, Rbond texture{pigment {color rgb <1.00, 0.05, 0.05> transmit 0.0} finish{ase3}}}
cylinder {<  0.93,   4.57,  -1.46>, <  0.93,   3.66,  -1.46>, Rbond texture{pigment {color rgb <0.40, 0.56, 0.56> transmit 0.0} finish{ase3}}}
cylinder {<  0.93,   2.74,  -1.46>, <  0.93,   3.66,  -1.46>, Rbond texture{pigment {color rgb <1.00, 0.05, 0.05> transmit 0.0} finish{ase3}}}
cylinder {<  0.93,   4.57,  -1.46>, <  0.35,   4.72,  -2.19>, Rbond texture{pigment {color rgb <0.40, 0.56, 0.56> transmit 0.0} finish{ase3}}}
cylinder {< -0.24,   4.87,  -2.92>, <  0.35,   4.72,  -2.19>, Rbond texture{pigment {color rgb <1.00, 0.05, 0.05> transmit 0.0} finish{ase3}}}
cylinder {<  0.93,   4.57,  -1.46>, <  0.35,   4.72,  -0.73>, Rbond texture{pigment {color rgb <0.40, 0.56, 0.56> transmit 0.0} finish{ase3}}}
cylinder {< -0.24,   4.87,  -0.00>, <  0.35,   4.72,  -0.73>, Rbond texture{pigment {color rgb <1.00, 0.05, 0.05> transmit 0.0} finish{ase3}}}
cylinder {<  0.93,   4.57,  -1.46>, <  1.52,   4.72,  -2.19>, Rbond texture{pigment {color rgb <0.40, 0.56, 0.56> transmit 0.0} finish{ase3}}}
cylinder {<  2.11,   4.87,  -2.92>, <  1.52,   4.72,  -2.19>, Rbond texture{pigment {color rgb <1.00, 0.05, 0.05> transmit 0.0} finish{ase3}}}
cylinder {<  0.93,   4.57,  -1.46>, <  1.52,   4.72,  -0.73>, Rbond texture{pigment {color rgb <0.40, 0.56, 0.56> transmit 0.0} finish{ase3}}}
cylinder {<  2.11,   4.87,  -0.00>, <  1.52,   4.72,  -0.73>, Rbond texture{pigment {color rgb <1.00, 0.05, 0.05> transmit 0.0} finish{ase3}}}
