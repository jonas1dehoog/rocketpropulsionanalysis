
def pump_power(dp, m_dot, rho, eta):
    """ Get the input drive power for a pump.

    Arguments:
        dp: Pump pressure rise [units: pascal].
        m_dot: Pump mass flow [units: kilogram seconds**-1].
        rho: Density of pumped fluid [units: kilogram meters**-3].
        eta: Pump efficiency [units: none].

    Reteurns: 
        The shaft power required to drive the pump [units: watt].
    """
    return 1 / eta * dp * m_dot / rho

def turbine_enthalpy(p_o, p_e, T_o, gamma, c_p):
    """ Get the specific enthalpy drop for a turbine.

    Arguments:
        p_o: Turbine inlet stagnation pressure [units: sae as p_e]. 
        p_e: Turbine exit pressure [units: same as p_o].
        T_o: Turbine inlet stagnation temperature [units: kelvin].
        gamma: Turbine working gas ratio of specific heats [units: none].
        c_p: working gas heat capacity at const pressure 
        [units: joule kilograme**-1 kelvin**-1].

    Returns:
        The specific enthalpy drop across the turbine [units: joule kilogram-1].
    """
    # Turbine specific enthalpy drop [units: joule kilograms**-1]
    return c_p * T_o * (1 - (p_e / p_o)**((gamma -1) / gamma))

def turbine_spout_velocity(p_o, p_e, T_o, gamma, c_p):
   """ Get the theoretical spouting velocity for a turbine.

   Arguments:
     p_o: Turbine inlet stagnation pressure [units: same as p_e]. 
     p_e: Turbine exit pressure [units: same as p_o].
     T_o: Turbine inlet stagnation temperature [units: kelvin].
     gamma: Turbine working gas ratio of specific heats (units: none]. 
     c_p: working gas heat capacity at const pressure
        [units: joule kilogram**-1 kelvin**-1].

   Returns:
     The theoretical spouting velocity c_o of the turbine [units: meter second**-2].
   """
   dh_turb = turbine_enthalpy(p_o, p_e, T_o, gamma, c_p)
   c_o = ((2 * dh_turb)**0.5)
   return c_o