#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" Main program execute generate_qr_code."""
from app.generate_qr import GenerateQR
from time import sleep, time


if __name__ == "__main__":
    print('Inicio Geração das images com os QR codes...')
    start_time = time()
    qr = GenerateQR()
    with open('input_data.txt') as f: # 
         for line in f:
             qr.parameters(line)
    end_time = time()
    elapsed_time = end_time - start_time
    print(f'Fim geração - Tempo: {elapsed_time} segundos')
    qr.close()