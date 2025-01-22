{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "9d88c9e5-66ca-420d-9999-a447ff430794",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Exercises 1-4"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "2b8d7113-37b4-470c-9f4b-dbed333ac9d4",
   "metadata": {},
   "outputs": [],
   "source": [
    "import argparse\n",
    "parser = argparse.ArgumentParser(description = \"Convert a SAM file to BED format.\")\n",
    "parser.add_argument('-i', \"--input_sam\", dest = 'infile', help = \"Path to the input SAM file\")\n",
    "parser.add_argument('-o', '--output_bed', dest = 'outfile', default = 'out.bed', help = \"Path to the output BED file\")\n",
    "args = parser.parse_args()\n",
    "\n",
    "import gzip\n",
    "\n",
    "def sam_to_bed(input_sam, output_bed):\n",
    "# Open the input SAM file for reading\n",
    "    with open(input_sam, 'r') as sam_file:\n",
    "        # Open the output BED file for writing\n",
    "        with gzip.open(output_bed, 'wt') as bed_file:\n",
    "            # Iterate over each line in the SAM file\n",
    "            for line in sam_file:\n",
    "                # Skip header lines (lines starting with '@')\n",
    "                if line.startswith('@'):\n",
    "                    continue\n",
    "                    \n",
    "                # Split the line into fields \n",
    "                fields = line.strip().split('\\t')\n",
    "                if fields[2] == '*':\n",
    "                    continue\n",
    "                \n",
    "                # Extract necessary fields for BED format:\n",
    "                # [0] QNAME: Query template NAME (read name)\n",
    "                # [2] RNAME: Reference sequence NAME (Chromosome)\n",
    "                # [3] POS: 1-based leftmost mapping POSition\n",
    "                # [9] SEQ: segment SEQuence\n",
    "                chrom = fields[2]  # RNAME\n",
    "                start = int(fields[3]) - 1  # POS (convert to 0-based)\n",
    "                end = start + len(fields[9])  # Calculate end based on read length\n",
    "                \n",
    "                # BED format fields: Chrom, Start, End, Name, Score, Strand\n",
    "                name = fields[0]  # QNAME\n",
    "                score = fields[4]  # MAPQ\n",
    "                strand = '-' if int(fields[1]) & 16 else '+'\n",
    "                \n",
    "                # Write the formatted BED line to the output file\n",
    "                bed_file.write(f\"{chrom}\\t{start}\\t{end}\\t{name}\\t{score}\\t{strand}\\n\")\n",
    "\n",
    "sam_to_bed(args.infile, args.outfile)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "8710a837-40f2-440c-b5f5-760780996229",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Run in the command line:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "01b9f64b-13b7-4d4a-8ae4-60bb30559130",
   "metadata": {},
   "outputs": [],
   "source": [
    "python /project/wolf6844/sam_to_bed.py --input_sam /project/shared/python/1_python_programming/cd4_subset.sam"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.11.3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
