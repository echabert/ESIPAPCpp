#include <iostream>
#include <TCanvas.h>
#include <TH1F.h>

int main()
{
  std::cout << "BEGIN Test" << std::endl;
  TCanvas * can = new TCanvas("can","can",600,600);
  TH1F * histo = new TH1F("histo","histo",100,-5,5);
  histo->FillRandom("gaus",10000);
  histo->Draw();
  can->SaveAs("image.jpg");
  std::cout << "END Test" << std::endl;
  return 42;
}
