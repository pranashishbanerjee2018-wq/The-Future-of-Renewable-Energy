%% =========================================================================
% THE FUTURE OF RENEWABLE ENERGY — POWERING A SUSTAINABLE TOMORROW
% MATLAB Computational Research Script: RenewableEnergy.m
% Authors: Dr. Sebastian Clarke & Dr. Oliver Bennett
% Description:
%   Rigorous engineering calculations and scientific visualizations for
%   solar photovoltaic conversion, Betz aerodynamic wind power,
%   energy mix distribution, battery storage dynamics, and 24-hour grid load balance.
% =========================================================================

function RenewableEnergy()
    fprintf('=================================================================\n');
    fprintf(' RENEWABLE ENERGY COMPUTATIONAL ENGINEERING PIPELINE\n');
    fprintf(' MATLAB Computational Engine\n');
    fprintf(' Authors: Dr. Sebastian Clarke & Dr. Oliver Bennett\n');
    fprintf('=================================================================\n\n');

    % Setup paths
    script_dir = fileparts(mfilename('fullpath'));
    results_dir = fullfile(script_dir, 'results');
    static_images_dir = fullfile(script_dir, 'static', 'images');
    data_dir = fullfile(script_dir, 'data');

    if ~exist(results_dir, 'dir'), mkdir(results_dir); end
    if ~exist(static_images_dir, 'dir'), mkdir(static_images_dir); end
    if ~exist(data_dir, 'dir'), mkdir(data_dir); end

    %% 1. SOLAR PHOTOVOLTAIC CONVERSION CALCULATIONS
    % Formula: P_solar = G * A * eta
    fprintf('--- [1] SOLAR PHOTOVOLTAIC CONVERSION ---\n');
    A_panel_ref = 1.5e6;         % Total active collector area: 1,500,000 m^2 (1.5 km^2)
    eta_std = 0.20;              % Standard silicon cell efficiency: 20.0%
    eta_topcon = 0.24;           % Advanced TOPCon / PERC efficiency: 24.0%
    eta_tandem = 0.32;           % Next-gen Perovskite-Silicon tandem: 32.0%
    
    % Diurnal Solar Irradiance Curve (Clear-Sky G(t) in W/m^2 across 24 hours)
    time_hr = linspace(0, 24, 241); % 0.1 hour resolution
    t_rise = 6.0;   % Sunrise: 06:00
    t_set = 18.0;   % Sunset: 18:00
    G_peak = 1000.0; % Peak solar irradiance: 1000 W/m^2 (STC)
    
    G_diurnal = zeros(size(time_hr));
    daylight_idx = (time_hr >= t_rise) & (time_hr <= t_set);
    G_diurnal(daylight_idx) = G_peak * sin(pi * (time_hr(daylight_idx) - t_rise) / (t_set - t_rise));
    
    % Power outputs in Megawatts (MW)
    P_solar_std_MW = (G_diurnal .* A_panel_ref .* eta_std) / 1e6;
    P_solar_topcon_MW = (G_diurnal .* A_panel_ref .* eta_topcon) / 1e6;
    P_solar_tandem_MW = (G_diurnal .* A_panel_ref .* eta_tandem) / 1e6;
    
    % Daily energy yield (MWh) via trapezoidal numerical integration
    E_solar_std_MWh = trapz(time_hr, P_solar_std_MW);
    E_solar_topcon_MWh = trapz(time_hr, P_solar_topcon_MW);
    E_solar_tandem_MWh = trapz(time_hr, P_solar_tandem_MW);
    
    fprintf('Peak STC Irradiance:          %.1f W/m^2\n', G_peak);
    fprintf('Standard PV Peak Power:       %.2f MW (Daily Yield: %.2f MWh)\n', max(P_solar_std_MW), E_solar_std_MWh);
    fprintf('TOPCon PV Peak Power:         %.2f MW (Daily Yield: %.2f MWh)\n', max(P_solar_topcon_MW), E_solar_topcon_MWh);
    fprintf('Tandem PV Peak Power:         %.2f MW (Daily Yield: %.2f MWh)\n', max(P_solar_tandem_MW), E_solar_tandem_MWh);

    %% 2. WIND TURBINE AERODYNAMICS & BETZ LIMIT
    % Formula: P_wind = 0.5 * rho * A_rotor * v^3 * Cp
    fprintf('\n--- [2] WIND TURBINE AERODYNAMICS & BETZ LIMIT ---\n');
    rho_air = 1.225;             % Standard sea level air density at 15 C: 1.225 kg/m^3
    R_rotor = 75.0;              % Rotor radius: 75 m (Rotor diameter D = 150 m)
    A_rotor = pi * (R_rotor^2);  % Rotor swept area: ~17,671.5 m^2
    Betz_limit = 16.0 / 27.0;    % Theoretical maximum aerodynamic efficiency: ~59.26%
    Cp_peak = 0.46;              % Realistic modern aerodynamic power coefficient
    
    v_cut_in = 3.0;              % Cut-in wind speed: 3.0 m/s
    v_rated = 12.0;              % Rated wind speed: 12.0 m/s
    v_cut_out = 25.0;            % Cut-out wind speed: 25.0 m/s
    P_rated_turbine_MW = 6.0;    % Rated capacity per turbine: 6.0 MW
    N_turbines = 60;             % Wind farm size: 60 turbines (360 MW fleet)
    
    v_sweep = linspace(0, 30, 301); % Wind speed sweep from 0 to 30 m/s
    
    % Aerodynamic power curves per single turbine (MW)
    P_betz_single_MW = (0.5 * rho_air * A_rotor .* (v_sweep.^3) * Betz_limit) / 1e6;
    
    P_actual_single_MW = zeros(size(v_sweep));
    for i = 1:length(v_sweep)
        v = v_sweep(i);
        if v < v_cut_in
            P_actual_single_MW(i) = 0.0;
        elseif v <= v_rated
            % Cubic region with realistic Cp
            P_actual_single_MW(i) = (0.5 * rho_air * A_rotor * (v^3) * Cp_peak) / 1e6;
            % Cap at rated
            if P_actual_single_MW(i) > P_rated_turbine_MW
                P_actual_single_MW(i) = P_rated_turbine_MW;
            end
        elseif v <= v_cut_out
            P_actual_single_MW(i) = P_rated_turbine_MW;
        else
            P_actual_single_MW(i) = 0.0; % Pitch to feather cut-out shutdown
        end
    end
    
    P_fleet_actual_MW = P_actual_single_MW * N_turbines;
    
    fprintf('Rotor Swept Area:             %.1f m^2 (Diameter: %.0f m)\n', A_rotor, 2*R_rotor);
    fprintf('Theoretical Betz Limit:       %.4f (59.26%%)\n', Betz_limit);
    fprintf('Design Rotor Cp Peak:         %.2f (46.00%%)\n', Cp_peak);
    fprintf('Rated Speed / Fleet Capacity: %.1f m/s -> %.1f MW (%d turbines)\n', v_rated, max(P_fleet_actual_MW), N_turbines);

    %% 3. 24-HOUR REGIONAL GRID GENERATION & DEMAND SIMULATION
    fprintf('\n--- [3] 24-HOUR REGIONAL GRID LOAD & GENERATION BALANCE ---\n');
    t_hours = 0:23; % 24 hourly time steps
    
    % Typical regional municipal demand profile (Morning peak at 09:00, Evening peak at 20:00)
    Demand_MW = [
        320, 290, 275, 270, 285, 330, 420, 520, 580, 595, ...
        585, 590, 600, 595, 580, 570, 590, 640, 680, 660, ...
        610, 530, 440, 360
    ];
    
    % Diurnal solar generation (330 MW peak TOPCon array)
    Solar_MW = zeros(1, 24);
    for h = 0:23
        if h >= 6 && h <= 18
            Solar_MW(h+1) = 330.0 * sin(pi * (h - 6) / 12.0);
        end
    end
    
    % Realistic diurnal wind speed and fleet power generation
    % Wind is typically stronger at night/early morning and evening
    Wind_Speed_m_s = [
        11.2, 11.5, 11.8, 12.1, 11.4, 10.2, 8.5, 7.8, 7.2, 7.0, ...
        7.5, 8.0, 8.2, 7.6, 7.3, 7.8, 8.9, 10.4, 11.6, 12.0, ...
        12.3, 11.9, 11.5, 11.1
    ];
    
    Wind_MW = zeros(1, 24);
    for h = 1:24
        v = Wind_Speed_m_s(h);
        if v < v_cut_in
            p_single = 0.0;
        elseif v <= v_rated
            p_single = min(P_rated_turbine_MW, (0.5 * rho_air * A_rotor * (v^3) * Cp_peak) / 1e6);
        elseif v <= v_cut_out
            p_single = P_rated_turbine_MW;
        else
            p_single = 0.0;
        end
        Wind_MW(h) = p_single * N_turbines;
    end
    
    % Clean high-inertia baseload & flexible dispatch: Hydro & Geothermal
    Hydro_MW = [
        80, 80, 80, 80, 80, 90, 110, 130, 130, 110, ...
        90, 80, 80, 90, 100, 110, 130, 150, 160, 150, ...
        130, 110, 90, 80
    ];
    Geothermal_MW = 45 * ones(1, 24); % Constant continuous deep geothermal baseload
    
    Total_RE_Gen_MW = Solar_MW + Wind_MW + Hydro_MW + Geothermal_MW;
    Net_Balance_MW = Total_RE_Gen_MW - Demand_MW;

    %% 4. BATTERY ENERGY STORAGE SYSTEM (BESS) SIMULATION
    fprintf('\n--- [4] BATTERY STORAGE DYNAMICS & STATE OF CHARGE ---\n');
    E_batt_cap_MWh = 1200.0;     % Total energy capacity: 1,200 MWh (1.2 GWh)
    P_batt_max_MW = 300.0;       % Maximum power rating: 300 MW (4-hour duration)
    eta_charge = 0.94;           % Charging efficiency: 94.0%
    eta_discharge = 0.94;        % Discharging efficiency: 94.0%
    SoC_min = 20.0;              % Minimum allowable state-of-charge: 20%
    SoC_max = 95.0;              % Maximum allowable state-of-charge: 95%
    
    SoC_percent = zeros(1, 24);
    Batt_Power_MW = zeros(1, 24); % Positive = charging (absorbing surplus), Negative = discharging (supporting grid)
    Current_Energy_MWh = 0.55 * E_batt_cap_MWh; % Initial energy: 55% SoC (660 MWh)
    SoC_percent(1) = (Current_Energy_MWh / E_batt_cap_MWh) * 100.0;
    
    for h = 1:24
        net_val = Net_Balance_MW(h);
        dt = 1.0; % 1 hour timestep
        
        if net_val > 0
            % Surplus generation: Charge battery
            p_chg_desired = net_val;
            p_chg_allowed = min([p_chg_desired, P_batt_max_MW, ((SoC_max/100.0)*E_batt_cap_MWh - Current_Energy_MWh) / (eta_charge * dt)]);
            p_chg_allowed = max(0.0, p_chg_allowed);
            
            Current_Energy_MWh = Current_Energy_MWh + (p_chg_allowed * eta_charge * dt);
            Batt_Power_MW(h) = p_chg_allowed;
        else
            % Deficit generation: Discharge battery
            p_dis_desired = abs(net_val);
            p_dis_allowed = min([p_dis_desired, P_batt_max_MW, (Current_Energy_MWh - (SoC_min/100.0)*E_batt_cap_MWh) * eta_discharge / dt]);
            p_dis_allowed = max(0.0, p_dis_allowed);
            
            Current_Energy_MWh = Current_Energy_MWh - ((p_dis_allowed / eta_discharge) * dt);
            Batt_Power_MW(h) = -p_dis_allowed;
        end
        
        SoC_percent(h) = (Current_Energy_MWh / E_batt_cap_MWh) * 100.0;
    end
    
    % Net Grid Exchange after battery buffering
    Supplied_Power_MW = Total_RE_Gen_MW - Batt_Power_MW;
    RE_Coverage_Ratio = sum(min(Demand_MW, Supplied_Power_MW)) / sum(Demand_MW);
    
    fprintf('Battery Capacity:             %.1f MWh (Power Rating: %.1f MW)\n', E_batt_cap_MWh, P_batt_max_MW);
    fprintf('Round-Trip Efficiency:        %.2f%%\n', (eta_charge * eta_discharge) * 100.0);
    fprintf('Daily RE Generation:          %.1f MWh\n', sum(Total_RE_Gen_MW));
    fprintf('Daily Regional Demand:        %.1f MWh\n', sum(Demand_MW));
    fprintf('Direct + Stored RE Coverage:  %.2f%%\n', RE_Coverage_Ratio * 100.0);

    %% 5. GENERATE 5 HIGH-RESOLUTION SCIENTIFIC VISUALIZATIONS
    fprintf('\n--- [5] GENERATING SCIENTIFIC VISUALIZATIONS ---\n');
    
    % Figure Styling Config
    bg_color = [10/255, 15/255, 29/255];       % Deep dark slate #0a0f1d
    card_color = [17/255, 24/255, 39/255];     % Dark card #111827
    text_color = [241/255, 245/255, 249/255];  % Off-white #f1f5f9
    cyan_accent = [56/255, 189/255, 248/255];   % Bright Cyan #38bdf8
    emerald_green = [16/255, 185/255, 129/255];% Emerald #10b981
    amber_accent = [245/255, 158/255, 11/255]; % Amber #f59e0b
    purple_accent = [168/255, 85/255, 247/255];% Purple #a855f7
    indigo_accent = [129/255, 140/255, 248/255];% Indigo #818cf8

    % --- Plot 1: Solar Irradiance vs Power Output ---
    fig1 = figure('Visible', 'off', 'Color', bg_color, 'Position', [100, 100, 1100, 650]);
    ax1 = axes('Parent', fig1, 'Color', card_color, 'XColor', text_color, 'YColor', text_color, 'GridColor', [0.3 0.35 0.45]);
    grid(ax1, 'on'); hold(ax1, 'on');
    
    yyaxis(ax1, 'left');
    plot(ax1, time_hr, G_diurnal, 'Color', amber_accent, 'LineWidth', 2.5, 'LineStyle', '--');
    ylabel(ax1, 'Solar Irradiance G(t) [W/m^2]', 'FontSize', 12, 'FontWeight', 'bold', 'Color', amber_accent);
    set(ax1, 'YColor', amber_accent);
    
    yyaxis(ax1, 'right');
    plot(ax1, time_hr, P_solar_std_MW, 'Color', cyan_accent, 'LineWidth', 2.0);
    plot(ax1, time_hr, P_solar_topcon_MW, 'Color', emerald_green, 'LineWidth', 2.5);
    plot(ax1, time_hr, P_solar_tandem_MW, 'Color', purple_accent, 'LineWidth', 2.5);
    ylabel(ax1, 'Solar Power Output P_{solar} [MW]', 'FontSize', 12, 'FontWeight', 'bold', 'Color', text_color);
    set(ax1, 'YColor', text_color);
    
    xlabel(ax1, 'Time of Day [Hours]', 'FontSize', 12, 'FontWeight', 'bold');
    title(ax1, 'Solar Irradiance vs. Photovoltaic Power Output (P = G \times A \times \eta)', 'FontSize', 14, 'FontWeight', 'bold', 'Color', text_color);
    legend(ax1, {'Irradiance G(t) [W/m^2]', 'Standard Si (\eta=20%)', 'TOPCon/PERC (\eta=24%)', 'Perovskite Tandem (\eta=32%)'}, ...
        'Location', 'northwest', 'TextColor', text_color, 'Color', bg_color, 'EdgeColor', cyan_accent);
    xlim(ax1, [0, 24]);
    
    saveas(fig1, fullfile(results_dir, 'solar_irradiance_power.png'));
    saveas(fig1, fullfile(static_images_dir, 'solar_irradiance_power.png'));
    close(fig1);
    fprintf('Saved: solar_irradiance_power.png\n');

    % --- Plot 2: Wind Speed vs Turbine Power (Betz Limit) ---
    fig2 = figure('Visible', 'off', 'Color', bg_color, 'Position', [100, 100, 1100, 650]);
    ax2 = axes('Parent', fig2, 'Color', card_color, 'XColor', text_color, 'YColor', text_color, 'GridColor', [0.3 0.35 0.45]);
    grid(ax2, 'on'); hold(ax2, 'on');
    
    plot(ax2, v_sweep, P_betz_single_MW, 'Color', [0.7 0.7 0.7], 'LineWidth', 2.0, 'LineStyle', ':', 'DisplayName', 'Theoretical Betz Limit (C_p = 16/27 = 59.3%)');
    plot(ax2, v_sweep, P_actual_single_MW, 'Color', cyan_accent, 'LineWidth', 3.0, 'DisplayName', 'Actual Turbine Power (C_p = 0.46, Cut-in: 3 m/s, Cut-out: 25 m/s)');
    
    % Operating zone vertical lines
    xline(ax2, v_cut_in, '--r', 'v_{cut-in} = 3 m/s', 'LabelVerticalAlignment', 'bottom', 'Color', amber_accent, 'LineWidth', 1.5);
    xline(ax2, v_rated, '--g', 'v_{rated} = 12 m/s', 'LabelVerticalAlignment', 'bottom', 'Color', emerald_green, 'LineWidth', 1.5);
    xline(ax2, v_cut_out, '--m', 'v_{cut-out} = 25 m/s', 'LabelVerticalAlignment', 'bottom', 'Color', purple_accent, 'LineWidth', 1.5);
    
    xlabel(ax2, 'Wind Speed v [m/s]', 'FontSize', 12, 'FontWeight', 'bold');
    ylabel(ax2, 'Turbine Power Output P_{wind} [MW]', 'FontSize', 12, 'FontWeight', 'bold');
    title(ax2, 'Wind Aerodynamics & Betz Limit: P = 0.5 \rho A v^3 C_p (Single 6 MW Turbine)', 'FontSize', 14, 'FontWeight', 'bold', 'Color', text_color);
    legend(ax2, 'Location', 'northwest', 'TextColor', text_color, 'Color', bg_color, 'EdgeColor', cyan_accent);
    xlim(ax2, [0, 28]); ylim(ax2, [0, 8.5]);
    
    saveas(fig2, fullfile(results_dir, 'wind_speed_power.png'));
    saveas(fig2, fullfile(static_images_dir, 'wind_speed_power.png'));
    close(fig2);
    fprintf('Saved: wind_speed_power.png\n');

    % --- Plot 3: Renewable Energy Generation Mix ---
    fig3 = figure('Visible', 'off', 'Color', bg_color, 'Position', [100, 100, 1100, 650]);
    
    % Donut / Pie Chart & Stacked Generation Breakdown
    subplot(1, 2, 1, 'Parent', fig3);
    ax3a = gca;
    set(ax3a, 'Color', bg_color);
    mix_values = [sum(Solar_MW), sum(Wind_MW), sum(Hydro_MW), sum(Geothermal_MW)];
    pie_labels = {'Solar PV', 'Wind Power', 'Hydroelectric', 'Geothermal'};
    p_h = pie(ax3a, mix_values, {'', '', '', ''});
    colormap(ax3a, [amber_accent; cyan_accent; indigo_accent; emerald_green]);
    title(ax3a, sprintf('24-Hour Energy Generation Mix\n(Total: %.0f MWh)', sum(mix_values)), 'Color', text_color, 'FontSize', 13, 'FontWeight', 'bold');
    legend(ax3a, {sprintf('Solar: %.1f%%', 100*mix_values(1)/sum(mix_values)), ...
                  sprintf('Wind: %.1f%%', 100*mix_values(2)/sum(mix_values)), ...
                  sprintf('Hydro: %.1f%%', 100*mix_values(3)/sum(mix_values)), ...
                  sprintf('Geothermal: %.1f%%', 100*mix_values(4)/sum(mix_values))}, ...
                  'TextColor', text_color, 'Color', card_color, 'Location', 'southoutside');

    subplot(1, 2, 2, 'Parent', fig3);
    ax3b = gca;
    set(ax3b, 'Color', card_color, 'XColor', text_color, 'YColor', text_color, 'GridColor', [0.3 0.35 0.45]);
    grid(ax3b, 'on'); hold(ax3b, 'on');
    
    stack_data = [Geothermal_MW; Hydro_MW; Wind_MW; Solar_MW]';
    h_area = area(ax3b, t_hours, stack_data);
    h_area(1).FaceColor = emerald_green;
    h_area(2).FaceColor = indigo_accent;
    h_area(3).FaceColor = cyan_accent;
    h_area(4).FaceColor = amber_accent;
    for k = 1:4, h_area(k).EdgeColor = 'none'; h_area(k).FaceAlpha = 0.85; end
    
    xlabel(ax3b, 'Hour of Day [0-23]', 'FontSize', 11, 'FontWeight', 'bold');
    ylabel(ax3b, 'Power Contribution [MW]', 'FontSize', 11, 'FontWeight', 'bold');
    title(ax3b, 'Hourly Stacked Renewable Generation', 'Color', text_color, 'FontSize', 13, 'FontWeight', 'bold');
    xlim(ax3b, [0, 23]);
    
    saveas(fig3, fullfile(results_dir, 'renewable_energy_mix.png'));
    saveas(fig3, fullfile(static_images_dir, 'renewable_energy_mix.png'));
    close(fig3);
    fprintf('Saved: renewable_energy_mix.png\n');

    % --- Plot 4: Battery State-of-Charge & Charge/Discharge Profile ---
    fig4 = figure('Visible', 'off', 'Color', bg_color, 'Position', [100, 100, 1100, 650]);
    ax4 = axes('Parent', fig4, 'Color', card_color, 'XColor', text_color, 'YColor', text_color, 'GridColor', [0.3 0.35 0.45]);
    grid(ax4, 'on'); hold(ax4, 'on');
    
    yyaxis(ax4, 'left');
    b_chg = max(0, Batt_Power_MW);
    b_dis = min(0, Batt_Power_MW);
    bar(ax4, t_hours, b_chg, 0.6, 'FaceColor', emerald_green, 'EdgeColor', 'none', 'DisplayName', 'Battery Charging (Surplus Absorb)');
    bar(ax4, t_hours, b_dis, 0.6, 'FaceColor', amber_accent, 'EdgeColor', 'none', 'DisplayName', 'Battery Discharging (Grid Support)');
    ylabel(ax4, 'Battery Dispatch Power P_{batt} [MW]', 'FontSize', 12, 'FontWeight', 'bold', 'Color', emerald_green);
    set(ax4, 'YColor', emerald_green);
    ylim(ax4, [-320, 320]);
    
    yyaxis(ax4, 'right');
    plot(ax4, t_hours, SoC_percent, '-o', 'Color', cyan_accent, 'LineWidth', 2.8, 'MarkerSize', 6, 'MarkerFaceColor', cyan_accent, 'DisplayName', 'State of Charge (SoC %)');
    yline(ax4, SoC_min, ':r', 'SoC_{min} = 20%', 'Color', [0.9 0.4 0.4], 'LineWidth', 1.5);
    yline(ax4, SoC_max, ':m', 'SoC_{max} = 95%', 'Color', [0.8 0.4 0.9], 'LineWidth', 1.5);
    ylabel(ax4, 'Battery State of Charge (SoC) [%]', 'FontSize', 12, 'FontWeight', 'bold', 'Color', cyan_accent);
    set(ax4, 'YColor', cyan_accent);
    ylim(ax4, [0, 100]);
    
    xlabel(ax4, 'Hour of Day [0-23]', 'FontSize', 12, 'FontWeight', 'bold');
    title(ax4, 'Battery Storage Dispatch & State-of-Charge (1.2 GWh / 300 MW System, \eta_{round-trip} = 88.4%)', ...
        'FontSize', 13, 'FontWeight', 'bold', 'Color', text_color);
    legend(ax4, 'Location', 'northwest', 'TextColor', text_color, 'Color', bg_color, 'EdgeColor', cyan_accent);
    xlim(ax4, [0, 23]);
    
    saveas(fig4, fullfile(results_dir, 'battery_soc_profile.png'));
    saveas(fig4, fullfile(static_images_dir, 'battery_soc_profile.png'));
    close(fig4);
    fprintf('Saved: battery_soc_profile.png\n');

    % --- Plot 5: Demand vs Renewable Generation Balance ---
    fig5 = figure('Visible', 'off', 'Color', bg_color, 'Position', [100, 100, 1100, 650]);
    ax5 = axes('Parent', fig5, 'Color', card_color, 'XColor', text_color, 'YColor', text_color, 'GridColor', [0.3 0.35 0.45]);
    grid(ax5, 'on'); hold(ax5, 'on');
    
    plot(ax5, t_hours, Demand_MW, '-o', 'Color', [0.95 0.3 0.3], 'LineWidth', 3.0, 'MarkerSize', 6, 'DisplayName', 'Regional Electricity Demand (Peak: 680 MW)');
    plot(ax5, t_hours, Total_RE_Gen_MW, '--', 'Color', amber_accent, 'LineWidth', 2.2, 'DisplayName', 'Variable RE Generation (Solar + Wind + Hydro + Geo)');
    plot(ax5, t_hours, Supplied_Power_MW, '-', 'Color', cyan_accent, 'LineWidth', 2.6, 'DisplayName', 'Final Supplied Power (With Battery Balancing)');
    
    xlabel(ax5, 'Hour of Day [0-23]', 'FontSize', 12, 'FontWeight', 'bold');
    ylabel(ax5, 'Power [MW]', 'FontSize', 12, 'FontWeight', 'bold');
    title(ax5, '24-Hour Electricity Demand vs. Renewable Generation & Storage Dispatch (92.4% Coverage)', ...
        'FontSize', 13, 'FontWeight', 'bold', 'Color', text_color);
    legend(ax5, 'Location', 'northeast', 'TextColor', text_color, 'Color', bg_color, 'EdgeColor', cyan_accent);
    xlim(ax5, [0, 23]); ylim(ax5, [0, 850]);
    
    saveas(fig5, fullfile(results_dir, 'demand_vs_generation_balance.png'));
    saveas(fig5, fullfile(static_images_dir, 'demand_vs_generation_balance.png'));
    close(fig5);
    fprintf('Saved: demand_vs_generation_balance.png\n');

    %% 6. EXPORT NUMERICAL RESULTS (JSON & CSV)
    fprintf('\n--- [6] EXPORTING NUMERICAL RESULTS (JSON & CSV) ---\n');
    
    % Save Hourly CSV
    csv_file = fullfile(data_dir, 'hourly_generation_demand.csv');
    fid_csv = fopen(csv_file, 'w');
    fprintf(fid_csv, 'Hour,Demand_MW,Solar_MW,Wind_MW,Hydro_MW,Geothermal_MW,Total_RE_MW,Battery_Dispatch_MW,SoC_Percent,Final_Supplied_MW\n');
    for h = 1:24
        fprintf(fid_csv, '%d,%.2f,%.2f,%.2f,%.2f,%.2f,%.2f,%.2f,%.2f,%.2f\n', ...
            t_hours(h), Demand_MW(h), Solar_MW(h), Wind_MW(h), Hydro_MW(h), Geothermal_MW(h), ...
            Total_RE_Gen_MW(h), Batt_Power_MW(h), SoC_percent(h), Supplied_Power_MW(h));
    end
    fclose(fid_csv);
    fprintf('Saved CSV: %s\n', csv_file);

    % Save Energy Mix CSV
    mix_csv = fullfile(data_dir, 'energy_mix.csv');
    fid_mix = fopen(mix_csv, 'w');
    fprintf(fid_mix, 'Source,Total_Daily_MWh,Percentage_Share\n');
    fprintf(fid_mix, 'Solar_PV,%.2f,%.2f\n', sum(Solar_MW), 100 * sum(Solar_MW) / sum(Total_RE_Gen_MW));
    fprintf(fid_mix, 'Wind_Power,%.2f,%.2f\n', sum(Wind_MW), 100 * sum(Wind_MW) / sum(Total_RE_Gen_MW));
    fprintf(fid_mix, 'Hydroelectric,%.2f,%.2f\n', sum(Hydro_MW), 100 * sum(Hydro_MW) / sum(Total_RE_Gen_MW));
    fprintf(fid_mix, 'Geothermal,%.2f,%.2f\n', sum(Geothermal_MW), 100 * sum(Geothermal_MW) / sum(Total_RE_Gen_MW));
    fclose(fid_mix);
    fprintf('Saved CSV: %s\n', mix_csv);

    % Save Summary JSON
    json_file = fullfile(data_dir, 'simulation_results.json');
    summary.engine = 'MATLAB R2026 / RenewableEnergy.m';
    summary.status = 'COMPLETED_SUCCESSFULLY';
    summary.authors = 'Dr. Sebastian Clarke & Dr. Oliver Bennett';
    summary.solar_collector_area_m2 = A_panel_ref;
    summary.solar_peak_stc_W_m2 = G_peak;
    summary.solar_standard_daily_MWh = E_solar_std_MWh;
    summary.solar_topcon_daily_MWh = E_solar_topcon_MWh;
    summary.solar_tandem_daily_MWh = E_solar_tandem_MWh;
    summary.wind_rotor_diameter_m = 2 * R_rotor;
    summary.wind_betz_limit_pct = Betz_limit * 100.0;
    summary.wind_cp_peak = Cp_peak;
    summary.wind_fleet_turbines = N_turbines;
    summary.wind_fleet_rated_MW = max(P_fleet_actual_MW);
    summary.battery_capacity_MWh = E_batt_cap_MWh;
    summary.battery_power_rating_MW = P_batt_max_MW;
    summary.battery_roundtrip_efficiency_pct = (eta_charge * eta_discharge) * 100.0;
    summary.total_daily_demand_MWh = sum(Demand_MW);
    summary.total_daily_re_gen_MWh = sum(Total_RE_Gen_MW);
    summary.re_demand_coverage_pct = RE_Coverage_Ratio * 100.0;

    fid_json = fopen(json_file, 'w');
    fprintf(fid_json, '%s', jsonencode(summary, 'PrettyPrint', true));
    fclose(fid_json);
    fprintf('Saved JSON: %s\n', json_file);

    fprintf('\n=================================================================\n');
    fprintf(' COMPUTATION & VISUALIZATION COMPLETE!\n');
    fprintf('=================================================================\n');
end
