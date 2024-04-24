module imem4(
    input [7:0] address,
    output [7:0] instruction
);

wire [7:0] memory [0:31];
assign memory[0] = 8'b01000101;
assign memory[1] = 8'b01011001;
assign memory[2] = 8'b00011000;
assign memory[3] = 8'b01011100;
assign memory[4] = 8'b00001101;
assign memory[5] = 8'b10110100;
assign memory[6] = 8'b01100000;
assign memory[7] = 8'b00011011;
assign memory[8] = 8'b10001100;
assign memory[9] = 8'b01001000;
assign memory[10] = 8'b00101100;
assign memory[11] = 8'b11000011;
assign instruction = memory[address];
endmodule
