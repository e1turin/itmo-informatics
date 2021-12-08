' Выполнил Тюрин Иван

Sub Кнопка1_Щелчок()
    ' Объявление переменных
    Dim rng As Range
    Dim condition1 As FormatCondition, condition2 As FormatCondition
    
    ' Выбираем диапозон
    Set rng = ActiveWorkbook.Worksheets("Лист1").Range("G4", "V7")

    ' Определяем условие для форматирования
    Set condition1 = rng.FormatConditions.Add(xlCellValue, xlEqual, "=0") ' Равные 0
    Set condition2 = rng.FormatConditions.Add(xlCellValue, xlEqual, "=1") ' Равные 1
    
    ' Устанавливаем стили для выбраных ячеек
    With condition1
    	.Interior.Color = vbGreen
    End With
    
    With condition2
    	.Interior.Color = vbRed
    End With
   
End Sub
