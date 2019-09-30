from scalar.units import LBF, OZF

def Wheel_Friction(Weight):
    coef_friction_turf=2.4429;
    coef_friction_track=0.8388;
    coef_friction_court=0.4843;
    est_coef_friction_runway=(coef_friction_track+coef_friction_court)/2
    print est_coef_friction_runway
    est_friction=Weight*est_coef_friction_runway*OZF/LBF
    return est_friction

if __name__ == '__main__':
    print Wheel_Friction(40*LBF)