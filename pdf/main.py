from fpdf import FPDF


pdf = FPDF()
pdf.add_page()

pdf.set_font("Helvetica", "B", 16)
pdf.cell(0, 10, txt="Computer Architecture and Organization Notes", ln=True, align="C")
pdf.set_font("Helvetica", "I", 10)
pdf.cell(0, 10, txt="(Questions 1 to 10)", ln=True, align="C")
pdf.ln(10)


content = [
    ("Q1. What is the Von Neumann architecture?", 
     "It is a computer design model where both data and instructions are stored in the same memory unit. It consists of a CPU (ALU + control unit), memory, and I/O devices connected via a common bus. Instructions are fetched and executed sequentially."),
    
    ("Q2. What is the difference between RISC and CISC?", 
     "RISC (Reduced Instruction Set Computer) uses a small, highly optimized set of instructions, executes in one clock cycle, and relies on software (compiler) for complex operations. CISC (Complex Instruction Set Computer) has a large instruction set with variable-length instructions and can perform multi-step operations in a single instruction. Example: ARM is RISC, x86 is CISC."),
    
    ("Q3. What are the components of the CPU?", 
     "The CPU consists of: (1) ALU (Arithmetic Logic Unit) - performs arithmetic and logical operations; (2) Control Unit (CU) - directs the operation of the processor; (3) Registers - small, fast storage (PC, IR, MAR, MDR, accumulator); (4) Cache - fast memory for frequently used data."),
    
    ("Q4. What is pipelining in CPU design?", 
     "Pipelining is a technique where multiple instruction phases (Fetch, Decode, Execute, Write-back) overlap in execution. While one instruction is being decoded, the next is being fetched - like an assembly line. It increases throughput but not individual instruction latency."),
    
    ("Q5. What are pipeline hazards? Name the types.", 
     "Pipeline hazards are situations that prevent the next instruction from executing in the next clock cycle. Types: (1) Structural hazard - hardware resource conflict; (2) Data hazard - instruction depends on result of a previous instruction still in pipeline; (3) Control hazard - caused by branch instructions. Solutions include stalling, forwarding, and branch prediction."),
    
    ("Q6. What is the memory hierarchy?", 
     "Memory hierarchy arranges storage from fastest/smallest to slowest/largest: Registers -> L1 Cache -> L2 Cache -> L3 Cache -> Main Memory (RAM) -> Secondary Storage (HDD/SSD) -> Tertiary (optical, tape). Higher levels are faster and more expensive per byte."),
    
    ("Q7. What is cache memory and what is its purpose?", 
     "Cache is a small, high-speed memory located between the CPU and main memory. It stores frequently accessed data and instructions to reduce average memory access time. Uses the principle of locality - temporal (recently used data likely reused) and spatial (nearby data likely needed soon)."),
    
    ("Q8. What is direct mapping in cache?", 
     "In direct mapping, each block of main memory maps to exactly one cache line using the formula: cache line = (block number) mod (number of cache lines). It is simple to implement but can cause frequent conflict misses if two blocks map to the same line."),
    
    ("Q9. Explain set-associative cache mapping.", 
     "Set-associative mapping is a compromise between direct and fully associative. Cache is divided into sets, each containing multiple lines (ways). A memory block maps to a specific set (like direct), but can be placed in any line within that set (like associative). 2-way, 4-way, 8-way are common."),
    
    ("Q10. What is virtual memory?", 
     "Virtual memory is a memory management technique that gives processes the illusion of having more memory than physically available. It uses disk space as an extension of RAM. Pages are swapped in/out as needed (demand paging). Managed via page tables and a TLB (Translation Lookaside Buffer).")
]

for question, answer in content:
    pdf.set_font("Helvetica", "B", 12)
    pdf.multi_cell(0, 8, txt=question)
    pdf.set_font("Helvetica", size=11)
    pdf.multi_cell(0, 7, txt=answer)
    pdf.ln(5) 


pdf.output("Computer_Architecture.pdf")
print("PDF generated successfully")