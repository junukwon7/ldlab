module imem3(
    input [7:0] address,
    output [7:0] instruction
);

wire [7:0] memory [0:31];
assign memory[0] = 8'b01000111;
assign memory[1] = 8'b01011001;
assign memory[2] = 8'b01111101;
assign memory[3] = 8'b01110001;
assign memory[4] = 8'b01011101;
assign memory[5] = 8'b01011001;
assign memory[6] = 8'b01101101;
assign memory[7] = 8'b01110001;
assign memory[8] = 8'b11000011;
assign instruction = memory[address];
endmodule
