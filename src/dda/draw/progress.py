from typing import Dict, ValuesView, Optional

import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.axes import Axes
import datetime

from dda.draw.aim import draw_aim

def visualize_progress(
        start_date: datetime.date, total_pages: int, pages_per_day_goal:int, input_data: Dict[str, int], save_path: Optional[str] = None
    ) -> Optional[tuple[tuple[ValuesView[str], ValuesView[int]], tuple[list[datetime.date], list[int]]]]:
    dates: DatetimeIndex
    pages: list[int]
    aim_dates, aim_pages = draw_aim(start_date, total_pages, pages_per_day_goal)
    plot_summation_list: list[int] = []
    pages_sum: int = total_pages
    for pages_day_actual in input_data.values():
        pages_sum -= pages_day_actual
        plot_summation_list.append(pages_sum)
    date_keys_actual: list[datetime.date] = [datetime.datetime.strptime(_date, "%Y-%m-%d").date() for _date in input_data.keys()]
    if save_path is not None:
        fig: Figure
        ax: Axes
        fig, ax = plt.subplots()
        ax.plot(aim_dates, aim_pages, 'r.', label='Aim')
        ax.plot(aim_dates, aim_pages, 'r-', alpha=0.5)
        ax.plot(date_keys_actual, plot_summation_list, 'b.', label='Progress')
        ax.plot(date_keys_actual, plot_summation_list, 'b-', alpha=0.5)
        ax.set_xlabel('Date')
        ax.set_ylabel('Pages Read')
        ax.set_title('Reading Progress')
        ax.legend()
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.savefig(save_file)
        plt.show()
    else:
        return (aim_dates, aim_pages), (date_keys_actual, plot_summation_list)

if __name__ == "__main__":
    save_file: str = "../../../tmp_files/progress.visualize_progress.png"

    def _create_dummy() -> Dict[str, int]:
        input_data: Dict[str, int] = {}

        today = datetime.date.today()
        for i in range(1, 11):
            date = today + datetime.timedelta(days=i)
            pages_read = i * 10
            input_data[str(date)] = pages_read

        return input_data
    
    input_data: Dict[str, int] = _create_dummy()
    print("="*10)
    print(input_data)
    print("="*10)

    _tmp = visualize_progress(datetime.date.today(), 590, 10, input_data)
    print(_tmp)
    visualize_progress(datetime.date.today(), 590, 10, input_data, save_file)
