///* Includes ------------------------------------------------------------------*/
//#include "stm8s.h"
//#include "stm8s_conf.h"
//#include "stm8s_exti.c"
//#include "stm8s_tim2.c"
//
//void TIM2_PWM1(uint16_t CCR1_Val_1);
//void TIM2_PWM2(uint16_t CCR1_Val_2);
//void TIM2_PWM3(uint16_t CCR1_Val_3);
//
///* Private defines -----------------------------------------------------------*/
///* Private function prototypes -----------------------------------------------*/
///* Private functions ---------------------------------------------------------*/
//void delay(uint16_t i)
//{
//  while(i>0)
//  {
//    i--;
//    nop();
//  }
//  
//}
////         - TIM2_CH1  pin (PD.4)
////         - TIM2_CH2  pin (PD.3)
////         - TIM2_CH3  pin (PA.3)
//static void TIM2_PWM1(uint16_t CCR1_Val_1)
//{
//  /* Time base configuration */
//  TIM2_TimeBaseInit(TIM2_PRESCALER_1, 999);
//  /* PWM1 Mode configuration: Channel1 */ 
//  TIM2_OC1Init(TIM2_OCMODE_PWM1, TIM2_OUTPUTSTATE_ENABLE,CCR1_Val_1, TIM2_OCPOLARITY_HIGH);
//  TIM2_OC1PreloadConfig(ENABLE);
//  TIM2_ARRPreloadConfig(ENABLE);
//
//  /* TIM2 enable counter */
//  TIM2_Cmd(ENABLE);
//}
//
//void sendstring(char *str)
//{
//  while(*str != '\0') {
//  UART1_SendData8(*str);
//  while (UART1_GetFlagStatus(UART1_FLAG_TXE) == RESET);
//    str++;
//  }
//}
//
//INTERRUPT_HANDLER(UART1_RX_IRQHandler, 18)
//{
//    uint8_t receive;
//    receive = UART1_ReceiveData8();
//      
//    switch (receive){
//        case 'a':     
//
//            GPIO_WriteHigh(GPIOC,GPIO_PIN_5);
//            sendstring("Lamp: ON!\n");
//            break;
//
//        case 'b':
//  
//            GPIO_WriteLow(GPIOC,GPIO_PIN_5);
//            sendstring("Lamp: OFF!\n");
//            break;
//            
//        case 'c':
//
//            sendstring("Fan: Mode 1!\n");
//            TIM2_PWM1(300);
//            break;
//            
//        case 'd':
//
//            sendstring("Fan: Mode 2!\n");
//            TIM2_PWM1(700);
//            break;
//            
//        case 'e':
//
//            sendstring("Fan: Mode 3!\n");
//            TIM2_PWM1(999);
//            break;   
//        
//        case 'f':
//
//            sendstring("Fan: OFF!\n");
//            TIM2_Cmd(DISABLE);
//            break;
//    }
//}
//
//
//void main(void)
//{ 
//    //cau hinh clock
//    CLK_HSIPrescalerConfig(CLK_PRESCALER_HSIDIV8);
//    //khi khong cau hinh se chay toc do 2MHz
//    //===============================================
//
//  
//  GPIO_Init(GPIOC,GPIO_PIN_5,GPIO_MODE_OUT_PP_LOW_FAST);
//
//  UART1_Init((uint32_t)9600, UART1_WORDLENGTH_8D, UART1_STOPBITS_1, UART1_PARITY_NO, UART1_SYNCMODE_CLOCK_DISABLE, UART1_MODE_TXRX_ENABLE);
//  UART1_ITConfig(UART1_IT_RXNE_OR , ENABLE);
//  UART1_Cmd(ENABLE);
//   enableInterrupts();
//  /* Infinite loop */
//  while (1)
//  {
//                  
//  }
//
//}
//
//#ifdef USE_FULL_ASSERT
//
///**
//  * @brief  Reports the name of the source file and the source line number
//  *   where the assert_param error has occurred.
//  * @param file: pointer to the source file name
//  * @param line: assert_param error line source number
//  * @retval : None
//  */
//void assert_failed(u8* file, u32 line)
//{
//  /* User can add his own implementation to report the file name and line number,
//     ex: printf("Wrong parameters value: file %s on line %d\r\n", file, line) */
//
//  /* Infinite loop */
//  while (1)
//  {
//    
//  }
//}
//#endif
//
//
/* Includes ------------------------------------------------------------------*/
#include "stm8s.h"
#include "stm8s_conf.h"
#include "stm8s_exti.c"
#include "stm8s_tim2.c"

void TIM2_PWM1(uint16_t CCR1_Val_1);

/* Private defines -----------------------------------------------------------*/
/* Private function prototypes -----------------------------------------------*/
/* Private functions ---------------------------------------------------------*/
void delay(uint16_t i)
{
  while(i>0)
  {
    i--;
    nop();
  }
  
}
//         - TIM2_CH1  pin (PD.4)
//         - TIM2_CH2  pin (PD.3)
//         - TIM2_CH3  pin (PA.3)
static void TIM2_PWM1(uint16_t CCR1_Val_1)
{
  /* Time base configuration */
  TIM2_TimeBaseInit(TIM2_PRESCALER_1, 999);
  /* PWM1 Mode configuration: Channel1 */ 
  TIM2_OC1Init(TIM2_OCMODE_PWM1, TIM2_OUTPUTSTATE_ENABLE,CCR1_Val_1, TIM2_OCPOLARITY_HIGH);
  TIM2_OC1PreloadConfig(ENABLE);
  TIM2_ARRPreloadConfig(ENABLE);

  /* TIM2 enable counter */
  TIM2_Cmd(ENABLE);
}

void sendstring(char *str)
{
  while(*str != '\0') {
  UART1_SendData8(*str);
  while (UART1_GetFlagStatus(UART1_FLAG_TXE) == RESET);
    str++;
  }
}

INTERRUPT_HANDLER(UART1_RX_IRQHandler, 18)
{
    uint8_t receive;
    receive = UART1_ReceiveData8();
      
    switch (receive){
        case 'a':     

            GPIO_WriteHigh(GPIOC,GPIO_PIN_5);
            sendstring("Lamp: ON!\n");
            break;

        case 'b':
  
            GPIO_WriteLow(GPIOC,GPIO_PIN_5);
            sendstring("Lamp: OFF!\n");
            break;
            
        case 'c':

            sendstring("Fan: Mode 1!\n");
            TIM2_PWM1(300);
            break;
            
        case 'd':

            sendstring("Fan: Mode 2!\n");
            TIM2_PWM1(500);
            break;
            
        case 'e':

            sendstring("Fan: Mode 3!\n");
            TIM2_PWM1(999);
            break;   
        
        case 'f':

            sendstring("Fan: OFF!\n");
            TIM2_Cmd(DISABLE);
            break;
    }
}


void main(void)
{ 
    //cau hinh clock
    CLK_HSIPrescalerConfig(CLK_PRESCALER_HSIDIV8);
    //khi khong cau hinh se chay toc do 2MHz
    //===============================================

  
  GPIO_Init(GPIOC,GPIO_PIN_5,GPIO_MODE_OUT_PP_LOW_FAST);

  UART1_Init((uint32_t)9600, UART1_WORDLENGTH_8D, UART1_STOPBITS_1, UART1_PARITY_NO, UART1_SYNCMODE_CLOCK_DISABLE, UART1_MODE_TXRX_ENABLE);
  UART1_ITConfig(UART1_IT_RXNE_OR , ENABLE);
  UART1_Cmd(ENABLE);
   enableInterrupts();
  /* Infinite loop */
  while (1)
  {
        TIM2_PWM1(300);
        //TIM2_Cmd(DISABLE);
  }

}

#ifdef USE_FULL_ASSERT

/**
  * @brief  Reports the name of the source file and the source line number
  *   where the assert_param error has occurred.
  * @param file: pointer to the source file name
  * @param line: assert_param error line source number
  * @retval : None
  */
void assert_failed(u8* file, u32 line)
{
  /* User can add his own implementation to report the file name and line number,
     ex: printf("Wrong parameters value: file %s on line %d\r\n", file, line) */

  /* Infinite loop */
  while (1)
  {
    
  }
}
#endif


