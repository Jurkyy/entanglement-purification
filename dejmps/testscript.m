a = 'p';
b = 'g';
c = '.txt';
arr = [string('0'), string('0.1'), string('0.2'), string('0.3'), string('0.4'), string('0.5'), string('0.6'), string('0.7'), string('0.8'), string('0.9'), string('1')];

successrate = [];
fidelities = [];
fidstd = [];
for i = 1: 11
    for j = 1 : 11
        filename = append(a, arr(i), b, arr(j), c);
        fileId = fopen(filename, 'r');
        formatspec = '%f %f';
        sizeA = [2, Inf];
        H = fscanf(fileId, formatspec, sizeA);
        H = H';
        temp = [];
        count = 0;
        for k = 1: length(H)
            if (H(k, 1) == 1)
                temp = [temp, H(k, 2)];
                count = count + 1;
            end
        end
        fidelities = [fidelities, mean(temp)];
        fidstd = [fidstd, std(temp)];
        successrate = [successrate, count/length(H)];
    end
end
successrate = successrate'
fidelities'
