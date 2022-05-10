%% Definitions
% The Scene and output files directories
directories = defineDirectories(); 
% The Camera and Simulation Settings
camera = defineSimulationSettings();
% The Radar Modulation Parameters
radarParameters = defineRadar(camera);


%% Plots
ch_antenna1 = radarData(:,1,1);
ch_antenna1_1 = fft(ch_antenna1,[]);
Ns_sequency = 1:250;
range_sequency = (radarParameters.Ns-Ns_sequency+1)*radarParameters.c/(2*radarParameters.B);
figure
plot(range_sequency, 10 * log10(abs(ch_antenna1_1)))
xlabel('range in [meters]');ylabel('power in [dB]');